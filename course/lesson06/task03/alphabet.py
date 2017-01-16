#!/usr/bin/python3
"""
Alphabet
--------
Print a number of times that each English character is used in ``alice.txt``.

.. hint::
    For this task and below a character case shall be ignored.
"""
import string


def count_letters(file_path):
    """
    Calculate character frequency in specified file

    Args:
        file_path (str): path to file

    Returns:
         dict(str, int) : dictionary with character frequency
    """
    result = dict()
    with open(file_path, mode='r', encoding='utf-8') as fd:
        for line in fd:
            for letter in line:
                if letter in string.ascii_letters:
                    result[letter.lower()] = result.get(letter.lower(), 0) + 1
    return result

if __name__ == "__main__":
    print(count_letters("../../alice.txt"))
