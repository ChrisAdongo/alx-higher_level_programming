#!/usr/bin/python3
"""
Contains the to_json_string function
"""

import json

def to_json_string(my_obj):
    """
    Returns the JSON representation of an object as a string.
    
    :param my_obj: The object to convert to JSON.
    :return: A string containing the JSON representation of the object.
    """
    try:
        json_string = json.dumps(my_obj)
        return json_string
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

if __name__ == "__main__":
    input_obj = input("Enter an object to convert to JSON: ")
    
    try:
        # Attempt to parse the input string as a Python object
        parsed_obj = eval(input_obj)
        
        # Convert the parsed object to a JSON string
        json_str = to_json_string(parsed_obj)
        
        if json_str:
            print("JSON representation:")
            print(json_str)
        else:
            print("Failed to convert to JSON.")
    except Exception as e:
        print(f"An error occurred: {e}")

