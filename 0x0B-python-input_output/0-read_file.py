#!/usr/bin/env python3
"""
Contains the read_file function
"""

def read_file(filename=""):
    """
    Reads a text file (UTF-8) and prints its contents to stdout.
    
    :param filename: The name of the file to read.
    """
    try:
        with open(filename, "r", encoding="utf-8") as file:
            print(file.read(), end="")
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    file_to_read = input("Enter the name of the file to read: ")
    read_file(file_to_read)

