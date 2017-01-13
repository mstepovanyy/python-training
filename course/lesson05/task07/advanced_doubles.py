#!/usr/bin/python3
"""
Print a number of all occurences of double characters in a file (e.g. ``ee``).
But tripples shall not count (e.g. ``eee`` shall not count).
"""
import re


def count_doubles(file_name):
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
    print('Number of doubles in file: {}'.format(count_doubles('../../alice.txt')))
