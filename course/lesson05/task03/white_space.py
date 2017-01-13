#!/usr/bin/python3
"""
Remove all leading and trailing white-space from a file and print a number of
modified lines.
"""
import re
from course.lesson05.task01.task01 import get_output_file


def strip(input_file_name):
    """
    Remove all leading and trailing white-spaces, from 'input_file_name'.
    And output result into into current directory.

    Args:
    input_file_name (str): path to input file

    Returns:
        int : number of modified lines.
    """
    modified_lines = 0
    pattern = re.compile(
        r"""^\s+ # strip all the leading whitespaces
        (.*) # group all in the middle except whitespaces
        \s*$ # strip all the trailing whitespaces
        """, re.VERBOSE)  # compile regexp into one line
    with open(input_file_name, mode="r", encoding="utf-8") as in_fd:
        with open(get_output_file(input_file_name), mode="w", encoding="utf-8") as out_fd:
            for line in in_fd.readlines():
                match = pattern.match(line)
                if match and len(match.group(1)) != len(line):
                    modified_lines += 1
                    out_fd.write(match.group(1))
                    out_fd.write("\n")
                else:
                    out_fd.write(line)
    return modified_lines

if __name__ == "__main__":
    print("Number of modified lines: ", strip("../../alice.txt"))