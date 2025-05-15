#!/usr/bin/python3
def text_indentation(text):
    """
    Prints a text with 2 new lines after each '.', '?', and ':' character.

    Args:
        text (str): The text to print.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    punctuation = {'.', '?', ':'}
    i = 0
    length = len(text)
    result = ""

    while i < length:
        char = text[i]
        result += char
        if char in punctuation:
            result += "\n\n"
            # Skip all spaces after punctuation
            i += 1
            while i < length and text[i] == ' ':
                i += 1
            continue
        i += 1

    # Print with no leading or trailing spaces on each line
    for line in result.split('\n'):
        print(line.strip())
