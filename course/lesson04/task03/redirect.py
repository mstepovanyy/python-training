#!/usr/bin/python3
"""
Write a program that redirects its standard input
into a standard output line by line (like a shell pipe operator).
"""

import sys


def redirect():
    """
    Redirects standard input into standard output
    """
    for line in sys.stdin:
        print(line, file=sys.stdout, end="")

if __name__ == "__main__":
    redirect()
