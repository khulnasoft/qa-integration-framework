# Copyright (C) 2015-2023, Khulnasoft Inc.
# Created by Khulnasoft, Inc. <info@khulnasoft.com>.
# This program is free software; you can redistribute it and/or modify it under the terms of GPLv2

import sys

from khulnasoft_testing.constants.platforms import WINDOWS


if sys.platform == WINDOWS:
    PREFIX = r'.*execd.*'
else:
    PREFIX = r'.*khulnasoft-execd.*'
