#!/usr/bin/env python3
"""
Contains the "append after" function
"""

def append_after(filename="", search_string="", new_string=""):
    """
    Appends "new_string" after a line containing "search_string" in "filename".

    :param filename: The name of the file to modify.
    :param search_string: The string to search for in each line.
    :param new_string: The string to append after the line containing "search_string".
    """
    updated_lines = []

    try:
        with open(filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        for line in lines:
            updated_lines.append(line)
            if search_string in line:
                updated_lines.append(new_string)

        with open(filename, 'w', encoding='utf-8') as file:
            file.writelines(updated_lines)
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    filename = input("Enter the name of the file to modify: ")
    search_string = input("Enter the search string: ")
    new_string = input("Enter the string to append: ")

    append_after(filename, search_string, new_string)

