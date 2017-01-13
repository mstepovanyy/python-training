#!/usr/bin/python3
"""
Print a number of numbers in a file;  each number shall count only once (e.g.
``1234`` shall count only once, not 4 times).
"""
import re


def count_numbers(file_name):
    """
    Count numbers in provided file, and return total amount of it.

    Args:
        file_name (str): path to a file

    Returns:
        int : number of numbers in file.
    """
    numbers = 0
    with open(file_name, mode='r', encoding='utf-8') as fd:
        for line in fd:
            numbers += len(re.findall(r'\d+', line))
    return numbers

if __name__ == '__main__':
    print("Numbers count in file: {}".format(count_numbers('../../alice.txt')))
