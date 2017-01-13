#!/usr/bin/python3
"""
Print a number of words in a file (words can be separated by either white space
or any separator (e.g. ``,`` or ``-``).  Pure integers shall not count but
identifiers consisting of a mix of characters and integers shall count).
"""
import re


def count_words(file_name):
    """
    Count number of words in specified file, integers is not counted.

    Args:
        file_name (str): path to file

    Returns:
        int : number of words in file
    """
    count = 0
    with open(file_name, mode='r', encoding='utf-8') as fd:
        for line in fd:
            count += len(re.findall(r'\b(\d*[a-zA-Z\']+\d*\w*)\b', line))

    return count


if __name__ == '__main__':
    print('Number of words in file: {}'.format(count_words('../../alice.txt')))
