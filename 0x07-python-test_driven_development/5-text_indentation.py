#!/usr/bin/python3
# 5-text_indentation.py
"""Defines a text-indentation function."""


def text_indentation(text):
    """Print text with two new lines after each '.', '?', and ':'.

    Args:
        text (string): The text to print.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    indent = 0  # Variable to track the indentation level
    for char in text:
        if char in ".?:":  # Check for punctuation characters
            print(char + "\n" * 2)  # Print the character followed by two newlines
            indent = 0  # Reset the indentation level
        elif char == "\n":
            indent = 0  # Reset the indentation level when a newline is encountered
        else:
            if char != ' ':
                print(" " * indent + char, end="")
            indent += 1

