"""
Copyright (C) 2015-2023, Khulnasoft Inc.
Created by Khulnasoft, Inc. <info@khulnasoft.com>.
This program is free software; you can redistribute it and/or modify it under the terms of GPLv2
"""
from pathlib import Path

from khulnasoft_testing.constants.paths.configurations import KHULNASOFT_API_CONFIGURATION_PATH, KHULNASOFT_SECURITY_CONFIGURATION_PATH
from khulnasoft_testing.constants.api import CONFIGURATION_TYPES
from khulnasoft_testing.utils.file import read_yaml, append_content_to_yaml, remove_file, truncate_file, write_file


def check_configuration_type(configuration_type: str) -> None:
    """Check if the configuration type is allowed.

    Args:
        configuration_type (str): Configuration type.

    Raises:
        RuntimeError: When the configuration type is not allowed.
    """
    if configuration_type not in CONFIGURATION_TYPES:
        raise RuntimeError(f"The chosen option is not allowed, use one of these: {CONFIGURATION_TYPES}")


def set_target_configuration_file(configuration_type: str) -> str:
    """Set the target configuration filepath where the actions will be performed.

    Args:
        configuration_type (str): Configuration type.

    Returns:
        khulnasoft_api_configuration_path (str): Path to the chosen Khulnasoft API configuration file.
    """
    check_configuration_type(configuration_type)
    configuration_files = {'base': KHULNASOFT_API_CONFIGURATION_PATH, 'security': KHULNASOFT_SECURITY_CONFIGURATION_PATH}
    khulnasoft_api_configuration_path = configuration_files[configuration_type]

    return khulnasoft_api_configuration_path


def get_configuration(configuration_type: str = 'base') -> dict:
    """Get current content from the chosen Khulnasoft API configuration file.

    Args:
        configuration_type (str): Choose file from which the configuration will be obtained.

    Returns:
        current_configuration (dict): Current content of the `api.yaml` file.
    """
    target_file = set_target_configuration_file(configuration_type)

    return read_yaml(target_file) if Path(target_file).exists() else None


def append_configuration(khulnasoft_api_configuration_content: dict, configuration_type: str = 'base') -> None:
    """Write a new configuration at the end of the Khulnasoft API configuration file.

    Args:
        configuration_type (str): Choose configuration file to be removed.
        khulnasoft_api_configuration_content (dict): Content to be written in the given file.
    """
    target_file = set_target_configuration_file(configuration_type)
    if not Path(target_file).exists():
        write_file(target_file)

    if khulnasoft_api_configuration_content is None:
        truncate_file(target_file)
    else:
        append_content_to_yaml(target_file, khulnasoft_api_configuration_content)


def delete_configuration_file(configuration_type: str = 'base') -> None:
    """Delete chosen Khulnasoft API configuration file.

    Args:
        configuration_type (str): Choose configuration file to be removed.
    """
    remove_file(set_target_configuration_file(configuration_type))
