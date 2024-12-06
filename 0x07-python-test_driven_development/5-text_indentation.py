#!/usr/bin/python3
"""This is Question 5 of 'indentation' """


def text_indentation(text):
    """
    Prints a text with 2 new lines after each '.', '?', and ':'.
    Args:
        text (str): The input text to format.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    result = ""
    for char in text:
        result += char
        if char in ".?:":
            result += "\n\n"

    # Print the result without leading/trailing spaces on each line
    print("\n".join([line.strip() for line in result.split("\n")]))
