"""
Copyright (C) 2015-2023, Khulnasoft Inc.
Created by Khulnasoft, Inc. <info@khulnasoft.com>.
This program is free software; you can redistribute it and/or modify it under the terms of GPLv2
"""
import os

from . import KHULNASOFT_PATH

# API paths that do not fit in `configurations`

# Folders
KHULNASOFT_API_FOLDER_PATH = os.path.join(KHULNASOFT_PATH, 'api')
KHULNASOFT_API_CONFIGURATION_FOLDER_PATH = os.path.join(KHULNASOFT_API_FOLDER_PATH, 'configuration')
KHULNASOFT_API_SECURITY_FOLDER_PATH = os.path.join(KHULNASOFT_API_CONFIGURATION_FOLDER_PATH, 'security')
KHULNASOFT_API_SCRIPTS_FOLDER_PATH = os.path.join(KHULNASOFT_API_FOLDER_PATH, 'scripts')

# API scripts paths
KHULNASOFT_API_SCRIPT = os.path.join(KHULNASOFT_API_SCRIPTS_FOLDER_PATH, 'khulnasoft-apid.py')

# Databases paths
RBAC_DATABASE_PATH = os.path.join(KHULNASOFT_API_SECURITY_FOLDER_PATH, 'rbac.db')

# SSL paths
KHULNASOFT_API_CERTIFICATE = os.path.join(KHULNASOFT_API_CONFIGURATION_FOLDER_PATH, 'ssl', 'server.crt')
