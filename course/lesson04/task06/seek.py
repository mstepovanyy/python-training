#!/usr/bin/python3
"""
Write a program that updates a current date and time
in a file's first line (stored in the first 50 characters).
A file shall be specified as a first argument.
Other file content than first 50 characters shall not be modified.
"""

import sys
import datetime


def update_date(file_name):
    """Read specified file, and update first 50 chars with current date"""
    with open(file_name, mode='r+b') as fd:
        fd.seek(0)
        time_str = '{0:<50}'.format(str(datetime.datetime.now()))
        fd.write(time_str.encode("utf-8"))

if __name__ == "__main__":
    if len(sys.argv) == 2:
        update_date(sys.argv[1])
    else:
        print("Error: incorrect number of arguments provided.(Expected 1 - file name)", file=sys.stderr)