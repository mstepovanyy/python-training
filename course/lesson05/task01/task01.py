#!/usr/bin/python3

"""
Remove all empty lines in a file and print a number of removed lines.
"""

import os
import re


def remove_empty_lines(file_name):
    """
    Removes empty lines in file, and output result into file
    with a name: file_name<task_number>.txt

    Args:
        file_name (str): path to input file
    """
    removed_lines = 0
    with open(file_name, mode="r", encoding="utf-8") as fd:
        with open(get_output_file(file_name), mode="w", encoding="utf-8") as ofd:
            for line in fd.readlines():
                if re.search("^$", line):
                    removed_lines += 1
                else:
                    ofd.write(line)
    print("Removed lines: {}".format(removed_lines))


def get_output_file(path):
    """
    Accepts input file, and based on this file - new file name is generated.

    Args:
        path (str): input file, will be parsed

    Returns:
        str : generated file name
    """
    root, _ = os.path.splitext(path)
    return os.path.basename(root) + get_task_number() + ".txt"


def get_task_number():
    """Returns task number"""
    matcher = re.match(".*\D(?P<number>\d*)$", os.path.abspath("."))
    return matcher.group("number")

if __name__ == "__main__":
    file_name = os.path.abspath("../../alice.txt")
    remove_empty_lines(file_name)
