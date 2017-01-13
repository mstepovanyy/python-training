#!/usr/bin/python3
"""
Print a number of vocal letters in first 100 lines of a file.
"""
import re


def count_vocals(file_name, start=0, end=100):
    """
    Count vocals in specified file

    Args:
        file_name (str): path to file
        start     (int): first line in file
        end       (int): last line in file

    Returns:
        int : number of vocals in file
    """
    vocals_number = 0
    with open(file_name, mode='r', encoding='utf-8') as fd:
        for line in fd.readlines()[start: end]:
            vocals_number += len(re.findall(r'[aeiouAEIOU]', line))
    return vocals_number

if __name__ == "__main__":
    print("Vocals count in file: {}".format(count_vocals('../../alice.txt', 0, 100)))
