#!/usr/bin/python3
"""
Packing and unpacking
---------------------
Write a function which returns a tuple of first 10 and last 10 characters of an
input string.  Use an output of that function to print the first 10, the last 10
characters of some string and their concatenation.
"""


def get_input_string():
    """Read input string, and return it."""
    return input("Enter input string: ")


def get_first_and_last(input_string):
    """Get the first 10, and last 10 characters,
    and returns them as a tuple

    Args:
        input_string (str): string that will be used as source

    Returns:
         (str, str): tuple of first and last 10 chars in specified string
    """
    return input_string[0: 10], input_string[-10:]

if __name__ == '__main__':
    first, last = get_first_and_last(get_input_string())
    print("First: {}".format(first))
    print("Last:  {}".format(last))
    print("Concatenation: {}".format("".join((first, last))))
