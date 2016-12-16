#!/usr/bin/python3
"""
Replace all blank lines (lines consisting of just a white space)
with an empty line and print a number of modified lines.
Initially empty lines (lines that were empty before a replacement)
shall not count.
"""

import os
import re
from course.lesson05.task01.task01 import get_output_file


def replace_blank(input_file):
    """
    Replaces blank lines with empty lines. Output number of modifications.

    Args:
        input_file (str): input file that will be processed.
    """
    removed_lines = 0
    with open(input_file, mode="r", encoding="utf-8") as fd:
        with open(get_output_file(input_file), mode="w", encoding="utf-8") as ofd:
            for line in fd.readlines():
                if re.search("^ +$", line):
                    removed_lines += 1
                    ofd.write("\n")
                else:
                    ofd.write(line)
    print("Removed lines: {}".format(removed_lines))


if __name__ == "__main__":
    file_name = os.path.abspath("../../alice.txt")
    replace_blank(file_name)
