#!/usr/bin/env python3
"""
Contains the load_from_json_file function
"""

import json

def load_from_json_file(filename):
    """
    Creates an object from a JSON file.
    
    :param filename: The name of the JSON file to read and convert to an object.
    :return: The Python object created from the JSON file.
    """
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            loaded_obj = json.load(file)
        return loaded_obj
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return None
    except json.JSONDecodeError as e:
        print(f"JSON decoding error: {e}")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

if __name__ == "__main__":
    file_to_load = input("Enter the name of the JSON file to load: ")
    
    loaded_object = load_from_json_file(file_to_load)
    
    if loaded_object is not None:
        print("Loaded object:")
        print(loaded_object)

