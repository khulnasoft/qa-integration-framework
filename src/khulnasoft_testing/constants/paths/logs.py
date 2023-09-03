# Copyright (C) 2015-2023, Khulnasoft Inc.
# Created by Khulnasoft, Inc. <info@khulnasoft.com>.
# This program is free software; you can redistribute it and/or modify it under the terms of GPLv2
import os
import sys

from khulnasoft_testing.constants.platforms import WINDOWS

from . import KHULNASOFT_PATH


BASE_LOGS_PATH = os.path.join(KHULNASOFT_PATH, 'logs')

if sys.platform == WINDOWS:
    BASE_LOGS_PATH = KHULNASOFT_PATH
    ACTIVE_RESPONSE_LOG_PATH = os.path.join(BASE_LOGS_PATH, 'active-response', 'active-responses.log')
else:
    ACTIVE_RESPONSE_LOG_PATH = os.path.join(BASE_LOGS_PATH, 'active-responses.log')

KHULNASOFT_LOG_PATH = os.path.join(BASE_LOGS_PATH, 'ossec.log')
ALERTS_LOG_PATH = os.path.join(BASE_LOGS_PATH, 'alerts', 'alerts.log')
ALERTS_JSON_PATH = os.path.join(BASE_LOGS_PATH, 'alerts', 'alerts.json')
ARCHIVES_LOG_PATH = os.path.join(BASE_LOGS_PATH, 'archives', 'archives.log')
ARCHIVES_JSON_PATH = os.path.join(BASE_LOGS_PATH, 'archives', 'archives.json')

# API logs paths
KHULNASOFT_API_LOG_FILE_PATH = os.path.join(BASE_LOGS_PATH, 'api.log')
KHULNASOFT_API_JSON_LOG_FILE_PATH = os.path.join(BASE_LOGS_PATH, 'api.json')
