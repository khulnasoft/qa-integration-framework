# Copyright (C) 2015-2023, Khulnasoft Inc.
# Created by Khulnasoft, Inc. <info@khulnasoft.com>.
# This program is free software; you can redistribute it and/or modify it under the terms of GPLv2

AGENT_DAEMON = 'khulnasoft-agentd'
AGENTLESS_DAEMON = 'khulnasoft-agentlessd'
ANALYSISD_DAEMON = 'khulnasoft-analysisd'
API_DAEMON = 'khulnasoft-apid'
CLUSTER_DAEMON = 'khulnasoft-clusterd'
CSYSLOG_DAEMON = 'khulnasoft-csyslogd'
EXEC_DAEMON = 'khulnasoft-execd'
INTEGRATOR_DAEMON = 'khulnasoft-integratord'
MAIL_DAEMON = 'khulnasoft-maild'
MODULES_DAEMON = 'khulnasoft-modulesd'
MONITOR_DAEMON = 'khulnasoft-monitord'
LOGCOLLECTOR_DAEMON = 'khulnasoft-logcollector'
REMOTE_DAEMON = 'khulnasoft-remoted'
SYSCHECK_DAEMON = 'khulnasoft-syscheckd'
KHULNASOFT_DB_DAEMON = 'khulnasoft-db'

KHULNASOFT_AGENT_DAEMONS = [AGENT_DAEMON,
                       EXEC_DAEMON,
                       MODULES_DAEMON,
                       LOGCOLLECTOR_DAEMON,
                       SYSCHECK_DAEMON]

KHULNASOFT_MANAGER_DAEMONS = [AGENTLESS_DAEMON,
                         ANALYSISD_DAEMON,
                         API_DAEMON,
                         CLUSTER_DAEMON,
                         CSYSLOG_DAEMON,
                         EXEC_DAEMON,
                         INTEGRATOR_DAEMON,
                         LOGCOLLECTOR_DAEMON,
                         MAIL_DAEMON,
                         MODULES_DAEMON,
                         MONITOR_DAEMON,
                         REMOTE_DAEMON,
                         SYSCHECK_DAEMON,
                         KHULNASOFT_DB_DAEMON]

API_DAEMONS_REQUIREMENTS = [API_DAEMON,
                            KHULNASOFT_DB_DAEMON,
                            EXEC_DAEMON,
                            ANALYSISD_DAEMON,
                            REMOTE_DAEMON,
                            MODULES_DAEMON]

KHULNASOFT_AGENT = 'khulnasoft-agent'
KHULNASOFT_MANAGER = 'khulnasoft-manager'

KHULNASOFT_AGENT_WIN = 'khulnasoft-agent.exe'
