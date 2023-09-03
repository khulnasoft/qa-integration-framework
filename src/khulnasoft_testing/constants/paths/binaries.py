# Copyright (C) 2015-2023, Khulnasoft Inc.
# Created by Khulnasoft, Inc. <info@khulnasoft.com>.
# This program is free software; you can redistribute it and/or modify it under the terms of GPLv2
import os
import sys

from khulnasoft_testing.constants.platforms import WINDOWS

from . import KHULNASOFT_PATH

if sys.platform == WINDOWS:
    BIN_PATH = KHULNASOFT_PATH
else:
    BIN_PATH = os.path.join(KHULNASOFT_PATH, 'bin')

KHULNASOFT_CONTROL_PATH = os.path.join(BIN_PATH, 'khulnasoft-control')
AGENT_AUTH_PATH = os.path.join(BIN_PATH, 'agent-auth')
ACTIVE_RESPONSE_BIN_PATH = os.path.join(KHULNASOFT_PATH, 'active-response', 'bin')
ACTIVE_RESPONSE_FIREWALL_DROP = os.path.join(ACTIVE_RESPONSE_BIN_PATH, 'firewall-drop')
MANAGE_AGENTS_BINARY = os.path.join(BIN_PATH, 'manage_agents')
