#!/usr/bin/python3
"""
Words Count
-----------
Print a statistics about ``alice.txt`` like a `wc` Unix command (number of
lines, words, and characters).

.. hint::
    For this task and below assume that an English word cannot be split over
    multiple lines using a hyphen;  and that a hyphen is a normal separator
    between words (e.g. a phrase ``in-line`` consists on two words).
"""
import re
import string


def wc(file_path):
    """
    Count statistics for provided file:
        count of lines in file
        count of words in file
        count of letters in file only in scope of string.ascii_letters

    Args:
        file_path (str): path to file

    Return:
         lines, words, letters: tuple of int
    """
    with open(file_path, mode='r', encoding='utf-8') as fd:
        lines = 0
        words = 0
        characters = 0

        for line in fd:
            lines += 1
            words += len(re.findall(r'\b(\d*[a-zA-Z\']+\d*\w*)\b', line))
            for letter in line:
                if letter in string.ascii_letters:
                    characters += 1
    return lines, words, characters

if __name__ == "__main__":
    print("{} {} {} {}".format(*wc('../../alice.txt'), '../../alice.txt'))
