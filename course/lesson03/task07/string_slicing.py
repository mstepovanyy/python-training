#!/usr/bin/python3
"""
Write a function which takes a string and returns
the first 10 characters off it concatenated with the last 10 characters.
"""


def slice_and_concatenate(input_str):
    """
    Takes input_str separate only first 10 chars, and last 10 chars.
    Concatenate resulted sub strings.
    In case input string has less then 10 chars,
    only string with length  == "len(input_str) * 2" will be generated

    Args:
        input_str(str): input string

    Returns:
        str: concatenated string with first
             10 chars, and latest 10 chars
    """
    return input_str[0:10] + input_str[-10:]

if __name__ == "__main__":
    print(slice_and_concatenate("some short sentence"))
    print(slice_and_concatenate("very long string that need to be concatenated"))
    print(slice_and_concatenate("exactly 10"))
    print(slice_and_concatenate("short"))
