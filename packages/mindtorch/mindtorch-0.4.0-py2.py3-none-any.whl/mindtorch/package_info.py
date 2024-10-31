#!/usr/bin/env python
# -*- coding: utf-8 -*-

MAJOR = 0
MINOR = 4
PATCH = 0
PRE_RELEASE = ''
# Use the following formatting: (major, minor, patch, prerelease)
VERSION = (MAJOR, MINOR, PATCH, PRE_RELEASE)

__version__ = version = '.'.join(map(str, VERSION[:3])) + ''.join(VERSION[3:])
