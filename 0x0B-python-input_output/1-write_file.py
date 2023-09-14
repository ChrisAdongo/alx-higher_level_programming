#!/usr/bin/python3
"""
Contains the write_file function
"""


def write_file(filename="", text=""):
    """
    Writes the given text to the specified file and returns the number of characters written.
    
    :param filename: The name of the file to write to.
    :param text: The text to write to the file.
    :return: The number of characters written to the file.
    """
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            chars_written = file.write(text)
            return chars_written
    except Exception as e:
        print(f"An error occurred: {e}")
        return -1

if __name__ == "__main__":
    file_to_write = input("Enter the name of the file to write to: ")
    text_to_write = input("Enter the text to write to the file: ")
    
    chars_written = write_file(file_to_write, text_to_write)
    
    if chars_written != -1:
        print(f"{chars_written} characters were written to '{file_to_write}'.")

