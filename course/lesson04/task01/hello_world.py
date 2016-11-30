#!/usr/bin/python3
"""
Write a simple application that writes a string Hello world
into a file specified as a command-line argument.
"""
import sys


def write_line(file, text):
    """
    Writes selected text into specified file

    Args:
        file(str):  file that will contain provided text,
                    all existing content in file will be overwritten.
        text(str): content of the file
    """
    with open(file, mode='w', encoding="utf-8") as a_file:
        a_file.write(text)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise ValueError("Usage: python hello_world.py filename.txt")
    write_line(sys.argv[1], "Hello world")
