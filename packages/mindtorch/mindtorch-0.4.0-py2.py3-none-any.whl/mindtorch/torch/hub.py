# Part of the code was borrowed from https://github.com/pytorch/pytorch/blob/v1.12.1/torch/hub.py

import errno
import hashlib
import json
import os
import re
import shutil
import sys
import tempfile
import zipfile
import importlib.util
from importlib.abc import Loader
from pathlib import Path
from typing import Callable, Dict, Optional, Union, Any
from urllib.error import HTTPError
from urllib.request import urlopen, Request
from urllib.parse import urlparse
from mindtorch.torch.logging import warning
from mindtorch.module_hooker import torch_disable, torch_pop
from .serialization import load as torch_load # noqa: F401

try:
    from tqdm.auto import tqdm  # automatically select proper tqdm submodule if available
except ImportError:
    try:
        from tqdm import tqdm
    except ImportError:
        # fake tqdm if it's not installed
        class tqdm():  # type: ignore[no-redef]

            def __init__(self, total=None, disable=False,
                         unit=None, unit_scale=None, unit_divisor=None):
                self.total = total
                self.disable = disable
                self.n = 0
                self.unit = unit
                self.unit_scale = unit_scale
                self.unit_divisor = unit_divisor
                # ignore unit, unit_scale, unit_divisor; they're just for real tqdm

            def update(self, n):
                if self.disable:
                    return

                self.n += n
                if self.total is None:
                    sys.stderr.write("\r{0:.1f} bytes".format(self.n))
                else:
                    sys.stderr.write("\r{0:.1f}%".format(
                        100 * self.n / float(self.total)))
                sys.stderr.flush()

            def close(self):
                self.disable = True

            def __enter__(self):
                return self

            def __exit__(self, exc_type, exc_val, exc_tb):
                if self.disable:
                    return

                sys.stderr.write('\n')

__all__ = [
    'download_url_to_file',
    'get_dir',
    'help',
    'list',
    'load',
    'load_state_dict_from_url',
    'set_dir',
]

# matches bfd8deac from resnet18-bfd8deac.pth
HASH_REGEX = re.compile(r'-([a-f0-9]*)\.')

_TRUSTED_REPO_OWNERS = ("facebookresearch", "facebookincubator", "pytorch", "fairinternal")
ENV_GITHUB_TOKEN = 'GITHUB_TOKEN'
ENV_TORCH_HOME = 'TORCH_HOME'
ENV_XDG_CACHE_HOME = 'XDG_CACHE_HOME'
DEFAULT_CACHE_DIR = '~/.cache'
VAR_DEPENDENCY = 'dependencies'
MODULE_HUBCONF = 'hubconf.py'
READ_DATA_CHUNK = 8192
_hub_dir = None


def _import_module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec is not None
    module = importlib.util.module_from_spec(spec)
    assert isinstance(spec.loader, Loader)
    spec.loader.exec_module(module)
    return module


def _remove_if_exists(path):
    if os.path.exists(path):
        if os.path.isfile(path):
            os.remove(path)
        else:
            shutil.rmtree(path)


def _git_archive_link(repo_owner, repo_name, ref):
    return f"https://github.com/{repo_owner}/{repo_name}/zipball/{ref}"


def _load_attr_from_module(module, func_name):
    # Check if callable is defined in the module
    if func_name not in dir(module):
        return None
    return getattr(module, func_name)


def _get_torch_home():
    torch_home = os.path.expanduser(
        os.getenv(ENV_TORCH_HOME,
                  os.path.join(os.getenv(ENV_XDG_CACHE_HOME,
                                         DEFAULT_CACHE_DIR), 'torch')))
    return torch_home


def _parse_repo_info(github):
    if ':' in github:
        repo_info, ref = github.split(':')
    else:
        repo_info, ref = github, None
    repo_owner, repo_name = repo_info.split('/')

    if ref is None:
        try:
            with urlopen(f"https://github.com/{repo_owner}/{repo_name}/tree/main/"):
                ref = 'main'
        except HTTPError as e:
            if e.code == 404:
                ref = 'master'
            else:
                raise
    return repo_owner, repo_name, ref


def _read_url(url):
    with urlopen(url) as r:
        return r.read().decode(r.headers.get_content_charset('utf-8'))


def _validate_not_a_forked_repo(repo_owner, repo_name, ref):
    # Use urlopen to avoid depending on local git.
    headers = {'Accept': 'application/vnd.github.v3+json'}
    token = os.environ.get(ENV_GITHUB_TOKEN)
    if token is not None:
        headers['Authorization'] = f'token {token}'
    for url_prefix in (
            f'https://api.github.com/repos/{repo_owner}/{repo_name}/branches',
            f'https://api.github.com/repos/{repo_owner}/{repo_name}/tags'):
        page = 0
        while True:
            page += 1
            url = f'{url_prefix}?per_page=100&page={page}'
            response = json.loads(_read_url(Request(url, headers=headers)))
            # Empty response means no more data to process
            if not response:
                break
            for br in response:
                if br['name'] == ref or br['commit']['sha'].startswith(ref):
                    return

    raise ValueError(f'Cannot find {ref} in https://github.com/{repo_owner}/{repo_name}. '
                     'If it\'s a commit from a forked repo, please call hub.load() with forked repo directly.')



def _get_cache_or_reload(github, force_reload, trust_repo, calling_fn, verbose=True, skip_validation=False):
    # Setup hub_dir to save downloaded files
    hub_dir = get_dir()
    if not os.path.exists(hub_dir):
        os.makedirs(hub_dir)
    # Parse github repo information
    repo_owner, repo_name, ref = _parse_repo_info(github)
    # Github allows branch name with slash '/',
    # this causes confusion with path on both Linux and Windows.
    # Backslash is not allowed in Github branch name so no need to
    # to worry about it.
    normalized_br = ref.replace('/', '_')
    # Github renames folder repo-v1.x.x to repo-1.x.x
    # We don't know the repo name before downloading the zip file
    # and inspect name from it.
    # To check if cached repo exists, we need to normalize folder names.
    owner_name_branch = '_'.join([repo_owner, repo_name, normalized_br])
    repo_dir = os.path.join(hub_dir, owner_name_branch)
    # Check that the repo is in the trusted list
    _check_repo_is_trusted(repo_owner, repo_name, owner_name_branch, trust_repo=trust_repo, calling_fn=calling_fn)

    use_cache = (not force_reload) and os.path.exists(repo_dir)

    if use_cache:
        if verbose:
            sys.stderr.write('Using cache found in {}\n'.format(repo_dir))
    else:
        # Validate the tag/branch is from the original repo instead of a forked repo
        if not skip_validation:
            _validate_not_a_forked_repo(repo_owner, repo_name, ref)

        cached_file = os.path.join(hub_dir, normalized_br + '.zip')
        _remove_if_exists(cached_file)

        try:
            url = _git_archive_link(repo_owner, repo_name, ref)
            sys.stderr.write('Downloading: \"{}\" to {}\n'.format(url, cached_file))
            download_url_to_file(url, cached_file, progress=False)
        except HTTPError as err:
            if err.code == 300:
                warning(
                    f"The ref {ref} is ambiguous. Perhaps it is both a tag and a branch in the repo? "
                    "Torchhub will now assume that it's a branch. "
                    "You can disambiguate tags and branches by explicitly passing refs/heads/branch_name or "
                    "refs/tags/tag_name as the ref. That might require using skip_validation=True."
                )
                disambiguated_branch_ref = f"refs/heads/{ref}"
                url = _git_archive_link(repo_owner, repo_name, ref=disambiguated_branch_ref)
                download_url_to_file(url, cached_file, progress=False)
            else:
                raise

        with zipfile.ZipFile(cached_file) as cached_zipfile:
            extraced_repo_name = cached_zipfile.infolist()[0].filename
            extracted_repo = os.path.join(hub_dir, extraced_repo_name)
            _remove_if_exists(extracted_repo)
            # Unzip the code and rename the base folder
            cached_zipfile.extractall(hub_dir)

        _remove_if_exists(cached_file)
        _remove_if_exists(repo_dir)
        shutil.move(extracted_repo, repo_dir)  # rename the repo

    return repo_dir

def _check_repo_is_trusted(repo_owner, repo_name, owner_name_branch, trust_repo, calling_fn="load"):
    hub_dir = get_dir()
    filepath = os.path.join(hub_dir, "trusted_list")

    if not os.path.exists(filepath):
        Path(filepath).touch()
    with open(filepath, 'r') as file:
        trusted_repos = tuple(line.strip() for line in file)

    trusted_repos_legacy = next(os.walk(hub_dir))[1]

    owner_name = '_'.join([repo_owner, repo_name])
    is_trusted = (
        owner_name in trusted_repos
        or owner_name_branch in trusted_repos_legacy
        or repo_owner in _TRUSTED_REPO_OWNERS
    )

    if trust_repo is None:
        if not is_trusted:
            warning(
                "You are about to download and run code from an untrusted repository. In a future release, this won't "
                "be allowed. To add the repository to your trusted list, change the command to {calling_fn}(..., "
                "trust_repo=False) and a command prompt will appear asking for an explicit confirmation of trust, "
                f"or {calling_fn}(..., trust_repo=True), which will assume that the prompt is to be answered with "
                f"'yes'. You can also use {calling_fn}(..., trust_repo='check') which will only prompt for "
                f"confirmation if the repo is not already trusted. This will eventually be the default behaviour")
        return

    if (trust_repo is False) or (trust_repo == "check" and not is_trusted):
        response = input(
            f"The repository {owner_name} does not belong to the list of trusted repositories and as "
            f"such cannot be downloaded. Do you trust this repository and wish to add it to the trusted "
            f"list of repositories (y/N)?")
        if response.lower() in ("y", "yes"):
            if is_trusted:
                print("The repository is already trusted.")
        elif response.lower() in ("n", "no", ""):
            raise Exception("Untrusted repository.")
        else:
            raise ValueError(f"Unrecognized response {response}.")

    # At this point we're sure that the user trusts the repo (or wants to trust it)
    if not is_trusted:
        with open(filepath, "a") as file:
            file.write(owner_name + "\n")


def _check_module_exists(name):
    return importlib.util.find_spec(name) is not None


def _check_dependencies(m):
    dependencies = _load_attr_from_module(m, VAR_DEPENDENCY)

    if dependencies is not None:
        missing_deps = [pkg for pkg in dependencies if not _check_module_exists(pkg)]
        if len(missing_deps):
            raise RuntimeError('Missing dependencies: {}'.format(', '.join(missing_deps)))


def _load_entry_from_hubconf(m, model):
    if not isinstance(model, str):
        raise ValueError('Invalid input: model should be a string of function name')
    _check_dependencies(m)

    func = _load_attr_from_module(m, model)

    if func is None or not callable(func):
        raise RuntimeError('Cannot find callable {} in hubconf'.format(model))

    return func


def get_dir():
    # Issue warning to move data if old env is set
    if os.getenv('TORCH_HUB'):
        warning('TORCH_HUB is deprecated, please use env TORCH_HOME instead')

    if _hub_dir is not None:
        return _hub_dir
    return os.path.join(_get_torch_home(), 'hub')


def set_dir(d):
    global _hub_dir
    _hub_dir = os.path.expanduser(d)


def list(github, force_reload=False, skip_validation=False, trust_repo=None):
    repo_dir = _get_cache_or_reload(github, force_reload, trust_repo, "list", verbose=True,
                                    skip_validation=skip_validation)

    sys.path.insert(0, repo_dir)

    hubconf_path = os.path.join(repo_dir, MODULE_HUBCONF)
    hub_module = _import_module(MODULE_HUBCONF, hubconf_path)

    sys.path.remove(repo_dir)

    # We take functions starts with '_' as internal helper functions
    entrypoints = [f for f in dir(hub_module) if callable(getattr(hub_module, f)) and not f.startswith('_')]

    return entrypoints


def help(github, model, force_reload=False, skip_validation=False, trust_repo=None):
    repo_dir = _get_cache_or_reload(github, force_reload, trust_repo, "help", verbose=True,
                                    skip_validation=skip_validation)

    sys.path.insert(0, repo_dir)

    hubconf_path = os.path.join(repo_dir, MODULE_HUBCONF)
    hub_module = _import_module(MODULE_HUBCONF, hubconf_path)

    sys.path.remove(repo_dir)

    entry = _load_entry_from_hubconf(hub_module, model)

    return entry.__doc__


def load(repo_or_dir, model, *args, source='github', trust_repo=None, force_reload=False, verbose=True,
         skip_validation=False,
         **kwargs):
    source = source.lower()

    if source not in ('github', 'local'):
        raise ValueError(
            f'Unknown source: "{source}". Allowed values: "github" | "local".')

    if source == 'github':
        repo_or_dir = _get_cache_or_reload(repo_or_dir, force_reload, trust_repo, "load",
                                           verbose=verbose, skip_validation=skip_validation)
    torch_disable()
    model = _load_local(repo_or_dir, model, *args, **kwargs)
    torch_pop()
    return model


def _load_local(hubconf_dir, model, *args, **kwargs):
    sys.path.insert(0, hubconf_dir)

    hubconf_path = os.path.join(hubconf_dir, MODULE_HUBCONF)
    hub_module = _import_module(MODULE_HUBCONF, hubconf_path)

    entry = _load_entry_from_hubconf(hub_module, model)
    model = entry(*args, **kwargs)

    sys.path.remove(hubconf_dir)

    return model


def download_url_to_file(url, dst, hash_prefix=None, progress=True):
    file_size = None
    req = Request(url, headers={"User-Agent": "torch.hub"})
    u = urlopen(req)
    meta = u.info()
    if hasattr(meta, 'getheaders'):
        content_length = meta.getheaders("Content-Length")
    else:
        content_length = meta.get_all("Content-Length")
    if content_length is not None and len(content_length) > 0:
        file_size = int(content_length[0])

    dst = os.path.expanduser(dst)
    dst_dir = os.path.dirname(dst)
    f = tempfile.NamedTemporaryFile(delete=False, dir=dst_dir)

    try:
        if hash_prefix is not None:
            sha256 = hashlib.sha256()
        with tqdm(total=file_size, disable=not progress,
                  unit='B', unit_scale=True, unit_divisor=1024) as pbar:
            while True:
                buffer = u.read(8192)
                if len(buffer) == 0:
                    break
                f.write(buffer)
                if hash_prefix is not None:
                    sha256.update(buffer)
                pbar.update(len(buffer))

        f.close()
        if hash_prefix is not None:
            digest = sha256.hexdigest()
            if digest[:len(hash_prefix)] != hash_prefix:
                raise RuntimeError('invalid hash value (expected "{}", got "{}")'
                                   .format(hash_prefix, digest))
        shutil.move(f.name, dst)
    finally:
        f.close()
        if os.path.exists(f.name):
            os.remove(f.name)


def _is_legacy_zip_format(filename):
    if zipfile.is_zipfile(filename):
        infolist = zipfile.ZipFile(filename).infolist()
        return len(infolist) == 1 and not infolist[0].is_dir()
    return False


def _legacy_zip_load(filename, model_dir, map_location):
    warning('Falling back to the old format < 1.6. This support will be ' \
            'deprecated in favor of default zipfile format introduced in 1.6. ' \
            'Please redo torch.save() to save it in the new zipfile format.')
    with zipfile.ZipFile(filename) as f:
        members = f.infolist()
        if len(members) != 1:
            raise RuntimeError(
                'Only one file(not dir) is allowed in the zipfile')
        f.extractall(model_dir)
        extraced_name = members[0].filename
        extracted_file = os.path.join(model_dir, extraced_name)
    return torch_load(extracted_file, map_location=map_location)


def load_state_dict_from_url(
    url: str,
    model_dir: Optional[str] = None,
    map_location: Optional[Union[Callable[[str], str], Dict[str, str]]] = None,
    progress: bool = True,
    check_hash: bool = False,
    file_name: Optional[str] = None
) -> Dict[str, Any]:
    if os.getenv('TORCH_MODEL_ZOO'):
        warning('TORCH_MODEL_ZOO is deprecated, please use env TORCH_HOME instead')

    if model_dir is None:
        hub_dir = get_dir()
        model_dir = os.path.join(hub_dir, 'checkpoints')

    try:
        os.makedirs(model_dir)
    except OSError as e:
        if e.errno == errno.EEXIST:
            # Directory already exists, ignore.
            pass
        else:
            # Unexpected OSError, re-raise.
            raise

    parts = urlparse(url)
    filename = os.path.basename(parts.path)
    if file_name is not None:
        filename = file_name
    cached_file = os.path.join(model_dir, filename)
    if not os.path.exists(cached_file):
        sys.stderr.write('Downloading: "{}" to {}\n'.format(url, cached_file))
        hash_prefix = None
        if check_hash:
            r = HASH_REGEX.search(filename)  # r is Optional[Match[str]]
            hash_prefix = r.group(1) if r else None
        download_url_to_file(url, cached_file, hash_prefix, progress=progress)

    if _is_legacy_zip_format(cached_file):
        return _legacy_zip_load(cached_file, model_dir, map_location)
    return torch_load(cached_file, map_location=map_location)
