"""
Copyright (C) 2015-2023, Khulnasoft Inc.
Created by Khulnasoft, Inc. <info@khulnasoft.com>.
This program is free software; you can redistribute it and/or modify it under the terms of GPLv2
"""
import os
import sys

from khulnasoft_testing.constants.platforms import WINDOWS

from . import KHULNASOFT_PATH
from khulnasoft_testing.constants.paths.api import KHULNASOFT_API_FOLDER_PATH, KHULNASOFT_API_SECURITY_FOLDER_PATH


if sys.platform == WINDOWS:
    BASE_CONF_PATH = KHULNASOFT_PATH
else:
    BASE_CONF_PATH = os.path.join(KHULNASOFT_PATH, 'etc')

KHULNASOFT_CLIENT_KEYS_PATH = os.path.join(BASE_CONF_PATH, 'client.keys')
SHARED_CONFIGURATIONS_PATH = os.path.join(BASE_CONF_PATH, 'shared')
KHULNASOFT_CONF_PATH = os.path.join(BASE_CONF_PATH, 'ossec.conf')
KHULNASOFT_LOCAL_INTERNAL_OPTIONS = os.path.join(BASE_CONF_PATH, 'local_internal_options.conf')
ACTIVE_RESPONSE_CONFIGURATION = os.path.join(SHARED_CONFIGURATIONS_PATH, 'ar.conf')
AR_CONF = os.path.join(SHARED_CONFIGURATIONS_PATH, 'ar.conf')
CUSTOM_RULES_PATH = os.path.join(BASE_CONF_PATH, 'rules')
CUSTOM_RULES_FILE = os.path.join(CUSTOM_RULES_PATH, 'local_rules.xml')

# Khulnasoft API configurations path
KHULNASOFT_API_CONFIGURATION_PATH = os.path.join(KHULNASOFT_API_FOLDER_PATH, 'configuration', 'api.yaml')
KHULNASOFT_SECURITY_CONFIGURATION_PATH = os.path.join(KHULNASOFT_API_SECURITY_FOLDER_PATH, 'security.yaml')
