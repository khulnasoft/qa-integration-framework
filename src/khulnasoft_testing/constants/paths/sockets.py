# Copyright (C) 2015-2023, Khulnasoft Inc.
# Created by Khulnasoft, Inc. <info@khulnasoft.com>.
# This program is free software; you can redistribute it and/or modify it under the terms of GPLv2
import os

from . import KHULNASOFT_PATH


QUEUE_CLUSTER_PATH = os.path.join(KHULNASOFT_PATH, 'queue', 'cluster')
QUEUE_DB_PATH = os.path.join(KHULNASOFT_PATH, 'queue', 'db')
QUEUE_SOCKETS_PATH = os.path.join(KHULNASOFT_PATH, 'queue', 'sockets')

ANALYSISD_ANALISIS_SOCKET_PATH = os.path.join(QUEUE_SOCKETS_PATH, 'analysis')
ANALYSISD_QUEUE_SOCKET_PATH = os.path.join(QUEUE_SOCKETS_PATH, 'queue')
AUTHD_SOCKET_PATH = os.path.join(QUEUE_SOCKETS_PATH, 'auth')
EXECD_SOCKET_PATH = os.path.join(QUEUE_SOCKETS_PATH, 'com')
LOGCOLLECTOR_SOCKET_PATH = os.path.join(QUEUE_SOCKETS_PATH, 'logcollector')
LOGTEST_SOCKET_PATH = os.path.join(QUEUE_SOCKETS_PATH, 'logtest')
MODULESD_WMODULES_SOCKET_PATH = os.path.join(QUEUE_SOCKETS_PATH, 'wmodules')
MODULESD_DOWNLOAD_SOCKET_PATH = os.path.join(QUEUE_SOCKETS_PATH, 'download')
MODULESD_CONTROL_SOCKET_PATH = os.path.join(QUEUE_SOCKETS_PATH, 'control')
MODULESD_KREQUEST_SOCKET_PATH = os.path.join(QUEUE_SOCKETS_PATH, 'krequest')
MODULESD_C_INTERNAL_SOCKET_PATH = os.path.join(QUEUE_CLUSTER_PATH, 'c-internal.sock')
MONITORD_SOCKET_PATH = os.path.join(QUEUE_SOCKETS_PATH, 'monitor')
REMOTED_SOCKET_PATH = os.path.join(QUEUE_SOCKETS_PATH, 'remote')
SYSCHECKD_SOCKET_PATH = os.path.join(QUEUE_SOCKETS_PATH, 'syscheck')
KHULNASOFT_DB_SOCKET_PATH = os.path.join(QUEUE_DB_PATH, 'wdb')

KHULNASOFT_SOCKETS = {
    'khulnasoft-agentd': [],
    'khulnasoft-apid': [],
    'khulnasoft-agentlessd': [],
    'khulnasoft-csyslogd': [],
    'khulnasoft-analysisd': [
        ANALYSISD_ANALISIS_SOCKET_PATH,
        ANALYSISD_QUEUE_SOCKET_PATH
    ],
    'khulnasoft-authd': [AUTHD_SOCKET_PATH],
    'khulnasoft-execd': [EXECD_SOCKET_PATH],
    'khulnasoft-logcollector': [LOGCOLLECTOR_SOCKET_PATH],
    'khulnasoft-monitord': [MONITORD_SOCKET_PATH],
    'khulnasoft-remoted': [REMOTED_SOCKET_PATH],
    'khulnasoft-maild': [],
    'khulnasoft-syscheckd': [SYSCHECKD_SOCKET_PATH],
    'khulnasoft-db': [KHULNASOFT_DB_SOCKET_PATH],
    'khulnasoft-modulesd': [
        MODULESD_WMODULES_SOCKET_PATH,
        MODULESD_DOWNLOAD_SOCKET_PATH,
        MODULESD_CONTROL_SOCKET_PATH,
        MODULESD_KREQUEST_SOCKET_PATH
    ],
    'khulnasoft-clusterd': [MODULESD_C_INTERNAL_SOCKET_PATH]
}

# These sockets do not exist with default Khulnasoft configuration
KHULNASOFT_OPTIONAL_SOCKETS = [
    MODULESD_KREQUEST_SOCKET_PATH,
    AUTHD_SOCKET_PATH
]
