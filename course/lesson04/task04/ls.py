#!/usr/bin/python3
"""
Write a program that lists all file names, their permissions, ownership,
last modified date in a specified directory (like an ls -l shell command).
If no directory is specified as the first (and only) command-line argument
than a current directory shall be listed. If more than one argument is passed
or the specified directory does not exist and application shall report
to standard error and return an error status code.
"""

import sys
import os
import stat
from datetime import datetime


def directory_list(path):
    """Output directory list in long format."""
    validate_path(path)
    for item in get_files(path):
        try:
            m_stat = os.stat(item)
            print("{access} {owner} {modified} {name}".format(
                name=os.path.split(item)[1],
                owner=m_stat.st_uid,
                modified=datetime.fromtimestamp(int(m_stat.st_mtime)),
                access=stat.filemode(m_stat.st_mode)
                )
            )
        except PermissionError:
            pass


def get_files(path):
    """Returns list of files/directories in specified folder."""
    return [os.path.join(path, item)for item in os.listdir(path)]


def validate_path(path):
    """Checks if provided path exist, and is directory"""
    if not os.path.exists(path):
        print("ERROR: Cannot find specified directory: " + path, file=sys.stderr)
        exit(1)
    if not os.path.isdir(path):
        print("ERROR: Provided object is not a directory: " + path, file=sys.stderr)
        exit(1)


if __name__ == "__main__":
    if len(sys.argv) == 2:
        directory_list(sys.argv[1])
    else:
        print("ERROR: invalid number of arguments\n"
              "Usage:\n\t{0} <directory>".format(sys.argv[0]), file=sys.stderr)
        exit(1)
