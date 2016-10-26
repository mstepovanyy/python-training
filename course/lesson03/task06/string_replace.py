#!/usr/bin/python3
"""
Write a function which takes a string and replaces
all vocal letters in it to an uppercase using a str.replace method.
"""


def string_replace(input_str):
    """
    Replaces all vocal letters with same letters in upper case.

    Args:
        input_str(str): input string

    Returns:
        str: input_str with replaced vocal letters.
    """

    for letter in "aeiouy":
        input_str = input_str.replace(letter, letter.upper())
    return input_str

if __name__ == "__main__":
    print(string_replace("to vocal"))
    print(string_replace("wtht vcl"))
    print(string_replace("oy oa"))
