"""
Copyright (C) 2015-2023, Khulnasoft Inc.
Created by Khulnasoft, Inc. <info@khulnasoft.com>.
This program is free software; you can redistribute it and/or modify it under the terms of GPLv2
"""
import os
import json
import socket
import time
from typing import List, Union

from khulnasoft_testing.constants.daemons import KHULNASOFT_DB_DAEMON
from khulnasoft_testing.constants.paths.sockets import QUEUE_DB_PATH, KHULNASOFT_DB_SOCKET_PATH
from khulnasoft_testing.tools.db_administrator import DatabaseAdministrator
from khulnasoft_testing.utils import services, secure_message


def delete_dbs():
    """Delete all khulnasoft-db databases."""
    for root, dirs, files in os.walk(QUEUE_DB_PATH):
        for file in files:
            os.remove(os.path.join(root, file))


def query_wdb(command) -> List[str]:
    """Make queries to khulnasoft-db using the wdb socket.

    Args:
        command (str): khulnasoft-db command alias. For example `global get-agent-info 000`.

    Returns:
        list: Query response data.
    """
    # If the wdb socket is not yet up, then wait or restart khulnasoft-db
    if not os.path.exists(KHULNASOFT_DB_SOCKET_PATH):
        max_retries = 6
        for _ in range(2):
            retry = 0
            # Wait if the wdb socket is not still alive (due to khulnasoft-db restarts). Max 3 seconds
            while not os.path.exists(KHULNASOFT_DB_SOCKET_PATH) and retry < max_retries:
                time.sleep(0.5)
                retry += 1

            # Restart khulnasoft-db in case of wdb socket is not yet up.
            if not os.path.exists(KHULNASOFT_DB_SOCKET_PATH):
                services.control_service('restart', daemon=KHULNASOFT_DB_DAEMON)

        # Raise custom exception if the socket is not up in the expected time, even restarting khulnasoft-db
        if not os.path.exists(KHULNASOFT_DB_SOCKET_PATH):
            raise Exception('The wdb socket is not up. khulnasoft-db was restarted but the socket was not found')

    # Create and open the socket connection with khulnasoft-db socket
    sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    sock.connect(KHULNASOFT_DB_SOCKET_PATH)
    data = []

    try:
        # Send the query request
        sock.send(secure_message.pack(len(command)) + command.encode())

        rcv = sock.recv(4)

        if len(rcv) == 4:
            data_len = secure_message.unpack(rcv)

            data = sock.recv(data_len).decode()

            # Remove response header and cast str to list of dictionaries
            # From --> 'ok [ {data1}, {data2}...]' To--> [ {data1}, data2}...]
            if len(data.split()) > 1 and data.split()[0] == 'ok':
                data = json.loads(' '.join(data.split(' ')[1:]))
    finally:
        sock.close()

    return data


def run_sql_script(database_path: Union[os.PathLike, str], script_path: Union[os.PathLike, str]) -> None:
    """Run SQL script in a database.

    Args:
        database_path (os.PathLike or str): Path to the SQLite database.
        script_path (os.PathLike or str): SQL script to be executed.
    """
    with DatabaseAdministrator(database_path) as db:
        db.execute_script(script_path)
