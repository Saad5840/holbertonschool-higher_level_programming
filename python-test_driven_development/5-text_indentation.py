#!/usr/bin/python3
"""
This module prints text with 2 new lines after each '.', '?', and ':'.
"""

def text_indentation(text):
    """
    Prints text with 2 new lines after specific punctuation marks.

    Args:
        text: Input string to format

    Raises:
        TypeError: If text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i = 0
    while i < len(text):
        if text[i] in ['.', '?', ':']:
            print(text[i], end="\n")
            # Skip any spaces immediately after punctuation
            i += 1
            while i < len(text) and text[i] == ' ':
                i += 1
            continue
        print(text[i], end="")
        i += 1
