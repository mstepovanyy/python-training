#!/usr/bin/python3
"""
Write a function that takes a comma-separated string
and returns a last element (separated by a last comma)
or the entire string if there is no comma in it.
"""


def split_string(input_str):
    """
    Parse input string and returns last comma separated element.
    In case no comma found, all string is returned.

    Args:
        input_str(str): input string that will be parsed

    Returns:
         str: last comma separated element,
              or all string in case no comma found.
    """
    return input_str.split(',')[-1]


if __name__ == '__main__':
    print(split_string("some, comma, separated, string."))
    print(split_string("some string without comma."))