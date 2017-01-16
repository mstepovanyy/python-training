#!/usr/bin/python3
"""
Words Usage
-----------
Print the first ``N`` most used English words in ``alice.txt``;  ``N`` shall be
a positive number taken from a command line.
"""
import re
import sys


def get_used_words(file_path, count):
    """
        Count  unique words in file, and return 'count' most used

        Args:
            file_path (str): path to file
            count (int): number of words to return

        Returns:
            dict(int, word): dictionary with usage, and word
        """

    words = dict()
    with open(file_path, mode='r', encoding='utf-8') as fd:
        for line in fd:
            for word in re.findall(r'\b(\d*[a-zA-Z\']+\d*\w*)\b', line):
                words[word.lower()] = words.get(word.lower(), 0) + 1
    return sorted(words.items(), key=lambda w: w[1], reverse=True)[0:count]


def read_words_count():
    """
    Read words count from command line

    Returns:
         int: number of words.
    """
    if len(sys.argv) == 2 and int(sys.argv[1]) > 0:
        return int(sys.argv[1])
    raise ValueError("Usage: {} <count> , count - number of words".format(sys.argv[0]))


if __name__ == "__main__":
    words_frequency = get_used_words('../../alice.txt', read_words_count())
    output_string = ["{}: {}".format(item[0], item[1]) for item in words_frequency]
    print("Most used words: \n{}".format("\n".join(output_string)))