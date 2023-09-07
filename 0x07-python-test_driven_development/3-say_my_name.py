#!/usr/bin/python3
# 3-say_my_name.py
"""Defines a name-printing function."""


def say_my_name(first_name, last_name=""):
    """Print a full name.

    Args:
        first_name (str): The first name to print.
        last_name (str, optional): The last name to print. Defaults to an empty string.

    Raises:
        TypeError: If either first_name or last_name are not strings.
    """
    if not isinstance(first_name, str) or not isinstance(last_name, str):
        raise TypeError("Both first_name and last_name must be strings")
    
    full_name = first_name
    if last_name:
        full_name += " " + last_name
    
    print("My name is", full_name)
