#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):
    """Deletes a key in a dictionary."""

    return {k: v for k, v in a_dictionary.items() if k != key}
