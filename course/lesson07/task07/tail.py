#!/usr/bin/python3
"""
Tail
----
Write a program that prints ``N`` last lines of a file in reverse order (just
like a ``tail -r`` FreeBSD command).  Both file name and a number of lines to
print shall be passed as command-line arguments.

Think of a memory-efficient yet fast way to implement this task.
"""
import sys
import os
import collections


def get_lines(file_name, lines_number):
    """
    Read data in the end of file. Return result in reversed order

    Args:
        file_name (str): path to file
        lines_number (int): number of lines at the end of file
    Returns:
        generator(str) : generator that will produce last lines in file in reversed order.
    """

    with open(file_name, mode='r', encoding='utf-8') as fd:
        for item in reversed(collections.deque(fd, maxlen=int(lines_number))):
            yield item.strip()


def is_int(value):
    """Checks that value inside String is an integer"""
    try:
        int(value)
        return True
    except:
        return False

if __name__ == '__main__':
    if len(sys.argv) == 3 and os.path.exists(sys.argv[1]) and is_int(sys.argv[2]):
        for line in get_lines(sys.argv[1], sys.argv[2]):
            print(line)
    else:
        print("Usage:\n\t{} <file_name> <lines_count>".format(sys.argv[0]))
