#!/usr/bin/python3
"""
Unique Words
------------
Print a number of unique English words in ``alice.txt``.
"""
import re


def count_unique(file_path):
    """
    Count number of unique words in file

    Args:
        file_path (str): path to file

    Returns:
        int: number of unique words
    """

    words = set()
    with open(file_path, mode='r', encoding='utf-8') as fd:
        for line in fd:
            for word in re.findall(r'\b(\d*[a-zA-Z\']+\d*\w*)\b', line):
                words.add(word.lower())
    return len(words)

if __name__ == "__main__":
    print("Number of unique words: {}".format(count_unique('../../alice.txt')))
