#!/usr/bin/python3
"""
Write a program that reads a user name from standard input
and prints Hello <name> input a standard output.
"""
import sys


def say_hello():
    """
    Read username from standart input,
    and prints hello message into standard output.
    """
    user_name = input("Your name: ")
    print("Hello {0}".format(user_name), file=sys.stdout)


if __name__ == "__main__":
    say_hello()
