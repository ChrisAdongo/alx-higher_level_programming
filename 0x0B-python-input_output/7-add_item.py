#!/usr/bin/python3
"""
Program to save strings from command line arguments to a file called "add_item.json".
The file contains a JSON serialized list of all strings entered as arguments to the program.
"""

import sys
import json

def create_or_load_json_file(filename):
    """
    Create the JSON file if it doesn't exist or load its content.
    
    :param filename: The name of the JSON file.
    :return: The data loaded from the JSON file.
    """
    try:
        with open(filename, 'a+') as file:
            if file.tell() == 0:
                json.dump([], file)
            else:
                file.seek(0)
                data = json.load(file)
        return data
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

def save_to_json_file(data, filename):
    """
    Save the data to the JSON file.
    
    :param data: The data to save.
    :param filename: The name of the JSON file.
    """
    try:
        with open(filename, 'w') as file:
            json.dump(data, file)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    filename = "add_item.json"
    file_data = create_or_load_json_file(filename)
    
    if len(sys.argv) > 1:
        file_data.extend(sys.argv[1:])
    
    save_to_json_file(file_data, filename)

