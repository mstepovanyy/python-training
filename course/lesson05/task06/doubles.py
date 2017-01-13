#!/usr/bin/python3
"""
Print a number of all occurences of double characters in a file (e.g. ``ee``).
"""
import re


def count_double_char(file_name):
    """
    Count double characters in file e.g. "ee"

    Args:
        file_name (str): path to file

    Returns:
        int : number of double chars in file
    """
    count = 0
    with open(file_name, mode='r', encoding='utf-8') as fd:
        for line in fd:
            count += len(re.findall(r'([a-zA-Z])\1', line))
    return count


if __name__ == '__main__':
    print("Number of double chars in file: {}".format(count_double_char('../../alice.txt')))
