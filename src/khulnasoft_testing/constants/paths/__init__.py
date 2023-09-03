# Copyright (C) 2015-2023, Khulnasoft Inc.
# Created by Khulnasoft, Inc. <info@khulnasoft.com>.
# This program is free software; you can redistribute it and/or modify it under the terms of GPLv2
import sys
import os

from khulnasoft_testing.constants.platforms import MACOS, WINDOWS


if sys.platform == WINDOWS:
    KHULNASOFT_PATH = os.path.join("C:", os.sep, "Program Files (x86)", "ossec-agent")
    ROOT_PREFIX = os.path.join('c:', os.sep)

elif sys.platform == MACOS:
    KHULNASOFT_PATH = os.path.join("/", "Library", "Ossec")
    ROOT_PREFIX = os.path.join('/', 'private', 'var', 'root')

else:
    KHULNASOFT_PATH = os.path.join("/", "var", "ossec")
    ROOT_PREFIX = os.sep
