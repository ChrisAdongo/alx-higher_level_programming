#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
    """Replace or add key/value pairs in a dictionary."""
    
    new_dictionary = {**a_dictionary, key: value}
    return (new_dictionary)
