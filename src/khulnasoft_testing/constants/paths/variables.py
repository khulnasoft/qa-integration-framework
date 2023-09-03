# Copyright (C) 2015-2023, Khulnasoft Inc.
# Created by Khulnasoft, Inc. <info@khulnasoft.com>.
# This program is free software; you can redistribute it and/or modify it under the terms of GPLv2
import os
import sys

from khulnasoft_testing.constants.platforms import WINDOWS

from . import KHULNASOFT_PATH


VAR_PATH = os.path.join(KHULNASOFT_PATH, 'var')
VAR_RUN_PATH = os.path.join(VAR_PATH, 'run')

ANALYSISD_STATE = os.path.join(VAR_RUN_PATH, 'khulnasoft-analysisd.state')

if sys.platform == WINDOWS:
    VERSION_FILE = os.path.join(KHULNASOFT_PATH, 'VERSION')
else:
    VERSION_FILE = ''
