#!/usr/bin/python3
"""
Print a number of sentences in a file (a sentence shall and in either a dot
``.`` or a tripple-dot ``...``.
"""
import re


def count_sentence(file_name):
    """
    Count number of sentence in file

    Args:
        file_name (str): path to file
    Returns:
        int : number of sentences
    """

    count = 0
    with open(file_name, mode='r', encoding='utf-8') as fd:
        for line in fd:
            count += len(re.findall(r'[\w*\s*][\\.]{3}|[\w*\s*][\\.]{1}', line))

    return count


if __name__ == '__main__':
    print("Number of sentence in file: {}".format(count_sentence('../../alice.txt')))
