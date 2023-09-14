#!/usr/bin/python3
"""
Contains the append_write function
"""


def append_write(filename="", text=""):
    """
    Appends the given text to the specified file and returns the number of characters appended.
    
    :param filename: The name of the file to append to.
    :param text: The text to append to the file.
    :return: The number of characters appended to the file.
    """
    try:
        with open(filename, 'a', encoding='utf-8') as file:
            chars_appended = file.write(text)
            return chars_appended
    except Exception as e:
        print(f"An error occurred: {e}")
        return -1

if __name__ == "__main__":
    file_to_append = input("Enter the name of the file to append to: ")
    text_to_append = input("Enter the text to append to the file: ")
    
    chars_appended = append_write(file_to_append, text_to_append)
    
    if chars_appended != -1:
        print(f"{chars_appended} characters were appended to '{file_to_append}'.")

