#!/usr/bin/python3
"""
Consumer
--------
Write a generator that consumes lines of a text and prints them to standard
output.  Use this generator and a `flatten` function from the previous task to
print contents of two different files to a screen pseudo-simultaneously.
"""
from course.lesson07.task05.flatten import flatten


def read_file(name):
    """
    Creates generator that returns lines from file

    Args:
        name(str): path to file

    Return:
        generator(str) : returns each line in file
    """
    with open(name, mode='r', encoding='utf-8') as fd:
        for line in fd:
            yield line.strip()


if __name__ == '__main__':
    for line in flatten(read_file('../../alice.txt'), read_file('../../alice.txt')):
        print(line)
