import sys
import importlib
from importlib.abc import MetaPathFinder

class ModuleHooker:
    loader_dict = dict()
    def __init__(self, orig_name, hook_name):
        self.orig_name = orig_name
        self.hook_name = hook_name
        self.module_dict = dict()
        self.torch_unique = dict()
        self.mindtorch_unique = dict()
        # `self.enabled = Ture` enable mindtorch. `self.enabled = False` enable torch
        self.enabled = False
        self.stack = list()

    def enable(self):
        self.stack.append(self.enabled)
        if self.enabled is False:
            self.enabled = True
            self.switch()

    def disable(self):
        self.stack.append(self.enabled)
        if self.enabled is True:
            self.enabled = False
            self.switch()

    def pop(self):
        prev_enabled = self.enabled
        if len(self.stack) == 0:
            self.enabled = False
        else:
            self.enabled = self.stack.pop()
        if prev_enabled is not self.enabled:
            self.switch()

    def sub_module(self, master, sub):
        return master == sub or sub.startswith(master + '.')

    def hook_module(self, name):
        return self.hook_name + name[len(self.orig_name):]

    def orig_module(self, name):
        return self.orig_name + name[len(self.hook_name):]

    def load(self, name, stop_reload):
        if self.sub_module(self.orig_name, name) and self.loaded(name) is False:
            self.module_dict[name] = ["__import__(name)", "__import__(self.hook_module(name))"]
        self.update(name, stop_reload)

    def loaded(self, name):
        return self.module_dict.get(name) is not None

    def switch(self):
        to_load = list()
        for k,v in sys.modules.items():
            if self.sub_module(self.orig_name, k):
                if self.loaded(k) is False:
                    self.module_dict[k] = ["__import__(name)", "__import__(self.hook_module(name))"]
                if self.enabled and isinstance(self.module_dict[k][0], str):
                    self.module_dict[k][0] = v
                if not(self.enabled) and isinstance(self.module_dict[k][1], str):
                    self.module_dict[k][1] = v
                to_load.append(k)
        to_load.sort()
        for k in to_load:
            if sys.modules.get(k) is not None:
                if self.enabled:
                    self.torch_unique[k] = sys.modules.get(k)
                else:
                    self.mindtorch_unique[k] = sys.modules.get(k)
                del sys.modules[k]
        for k in to_load:
            self.load(k, False)
        if self.enabled:
            sys.modules.update(self.mindtorch_unique)
        else:
            sys.modules.update(self.torch_unique)

    def create_module(loader, spec):
        if spec is not None and spec.loader is not None and ModuleHooker.loader_dict.get(spec.loader) is not None:
            spec.loader.create_module = ModuleHooker.loader_dict[spec.loader][1]
            return ModuleHooker.loader_dict[spec.loader][2]
        return None

    def exec_module(loader, module):
        if module is not None and module.__spec__ is not None and module.__spec__.loader is not None \
            and ModuleHooker.loader_dict.get(module.__spec__.loader) is not None:
            module.__spec__.loader.exec_module = ModuleHooker.loader_dict[module.__spec__.loader][0]

    def update(self, name, stop_reload):
        if self.enabled and isinstance(self.module_dict[name][1], str):
            if sys.modules.get(self.hook_module(name)) is None:
                try:
                    __import__(self.hook_module(name))
                except ImportError:
                    if stop_reload:
                        print("Fail to import ", self.hook_module(name))
                    return
            m = sys.modules[self.hook_module(name)]
            if stop_reload and m.__spec__ is not None and m.__spec__.loader is not None:
                ModuleHooker.loader_dict[m.__spec__.loader] = [m.__spec__.loader.exec_module, m.__spec__.loader.create_module, m]
                m.__spec__.loader.exec_module = self.exec_module
                m.__spec__.loader.create_module = self.create_module
            self.module_dict[name][1] = sys.modules[self.hook_module(name)]
        if not(self.enabled) and isinstance(self.module_dict[name][0], str):
            if sys.modules.get(name) is None:
                try:
                    __import__(name)
                except ImportError:
                    if stop_reload:
                        print("Fail to import ", name)
                    return
            m = sys.modules[name]
            if stop_reload and m.__spec__ is not None and m.__spec__.loader is not None:
                ModuleHooker.loader_dict[m.__spec__.loader] = [m.__spec__.loader.exec_module, m.__spec__.loader.create_module, m]
                m.__spec__.loader.exec_module = self.exec_module
                m.__spec__.loader.create_module = self.create_module
            self.module_dict[name][0] = sys.modules[name]
        sys.modules[name] = self.module_dict[name][1 if self.enabled else 0]

class ModuleLoader(MetaPathFinder):

    module_list = dict()

    def regist(orig_name, hook_name):
        if ModuleLoader.module_list.get(orig_name) is None:
            ModuleLoader.module_list[orig_name] = ModuleHooker(orig_name, hook_name)
        return ModuleLoader.module_list[orig_name]

    def is_registed(orig_name):
        if ModuleLoader.module_list.get(orig_name) is None:
            return False
        else:
            return True

    def enabled(orig_name):
        if ModuleLoader.is_registed(orig_name):
            return ModuleLoader.module_list[orig_name].enabled
        return False

    def find_spec(fullname, path=None, tar=None):
        if fullname.endswith("._"):
            return None
        for k,v in ModuleLoader.module_list.items():
            if v.sub_module(v.hook_name, fullname):
                newname = v.orig_module(fullname)
                fullname = newname
                break
        for k,v in ModuleLoader.module_list.items():
            if v.enabled and v.sub_module(k, fullname) and v.loaded(fullname) is False:
                v.load(fullname, True)
                try:
                    result = sys.modules[fullname]
                except KeyError as e:
                    raise ModuleNotFoundError(repr(e))
                return result
        return None

sys.meta_path.insert(0, ModuleLoader)

def module_hook(orig, hooker, enable):
    module = ModuleLoader.regist(orig, hooker)
    if enable:
        module.enable()
    else:
        module.disable()

def module_pop(orig, hooker):
    module = ModuleLoader.regist(orig, hooker)
    module.pop()

torch_dict = {"torch": "mindtorch.torch", "torchvision": "mindtorch.torchvision", "torchaudio": "mindtorch.torchaudio"}


# Import torch instead of mindtorch
def torch_enable():
    for key,value in torch_dict.items():
        module_hook(key, value, False)

# Import mindtorch instead of torch
def torch_disable():
    for key,value in torch_dict.items():
        module_hook(key, value, True)

def torch_pop():
    for key,value in torch_dict.items():
        module_pop(key, value)
