#!/usr/bin/python3
"""
Contains the save_to_json_file function
"""

import json

def save_to_json_file(my_obj, filename):
    """
    Writes an object to a text file using a JSON representation.
    
    :param my_obj: The object to be saved to the file.
    :param filename: The name of the file where the JSON representation will be saved.
    """
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(my_obj, file)
        print(f"Object saved to '{filename}' as JSON.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    obj_to_save = input("Enter an object (e.g., dictionary) to save as JSON: ")
    file_to_save = input("Enter the name of the file to save to: ")
    
    try:
        # Attempt to parse the input as a Python object
        parsed_obj = eval(obj_to_save)
        
        # Save the parsed object as JSON to the specified file
        save_to_json_file(parsed_obj, file_to_save)
    except Exception as e:
        print(f"An error occurred: {e}")

