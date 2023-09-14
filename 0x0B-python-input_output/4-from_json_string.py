#!/usr/bin/python3
"""
Contains the from_json_string function
"""

import json

def from_json_string(my_str):
    """
    Returns an object represented by a JSON string.
    
    :param my_str: The JSON string to parse and convert to an object.
    :return: The Python object represented by the JSON string.
    """
    try:
        parsed_obj = json.loads(my_str)
        return parsed_obj
    except json.JSONDecodeError as e:
        print(f"JSON decoding error: {e}")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

if __name__ == "__main__":
    input_json_str = input("Enter a JSON string: ")
    
    try:
        parsed_object = from_json_string(input_json_str)
        
        if parsed_object is not None:
            print("Parsed object:")
            print(parsed_object)
        else:
            print("Failed to parse JSON string.")
    except Exception as e:
        print(f"An error occurred: {e}")

