# Copyright (C) 2015-2023, Khulnasoft Inc.
# Created by Khulnasoft, Inc. <info@khulnasoft.com>.
# This program is free software; you can redistribute it and/or modify it under the terms of GPLv2
import os

from khulnasoft_testing.constants.paths.sockets import QUEUE_SOCKETS_PATH, KHULNASOFT_DB_SOCKET_PATH, \
                                                  MODULESD_C_INTERNAL_SOCKET_PATH


def delete_sockets(path=None):
    """Delete a list of Khulnasoft socket files or all of them if None is specified.

    Args:
        path (list, optional): Absolute socket path. Default `None`.
    """
    try:
        if path is None:
            path = QUEUE_SOCKETS_PATH
            for file in os.listdir(path):
                os.remove(os.path.join(path, file))
            if os.path.exists(KHULNASOFT_DB_SOCKET_PATH):
                os.remove(KHULNASOFT_DB_SOCKET_PATH)
            if os.path.exists(MODULESD_C_INTERNAL_SOCKET_PATH):
                os.remove(MODULESD_C_INTERNAL_SOCKET_PATH)
        else:
            for item in path:
                os.remove(item)
    except FileNotFoundError:
        pass
