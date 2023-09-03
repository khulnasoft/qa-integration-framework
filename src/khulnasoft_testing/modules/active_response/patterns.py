# Copyright (C) 2015-2021, Khulnasoft Inc.
# Created by Khulnasoft, Inc. <info@khulnasoft.com>.
# This program is free software; you can redistribute it and/or modify it under the terms of GPLv2


# Callback patterns to find events in active-response.log file.
ACTIVE_RESPONSE_STARTING = r'Starting'
ACTIVE_RESPONSE_CANNOT_READ_SRCIP = r'.*Cannot read \'srcip\' from data'
ACTIVE_RESPONSE_RESTART_KHULNASOFT = r'.*active-response/bin/restart-khulnasoft.*'
ACTIVE_RESPONSE_FIREWALL_DROP = r'.*active-response/bin/firewall-drop.*'
ACTIVE_RESPONSE_INVALID_COMMAND = r'.*Cannot read \'srcip\' from data'
ACTIVE_RESPONSE_ADD_COMMAND = r'.*"command":"add".*'
ACTIVE_RESPONSE_DELETE_COMMAND = r'.*"command":"delete".*'
