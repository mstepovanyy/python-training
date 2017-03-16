#!/usr/bin/python3
"""
Write a context manager class that takes an object, its attribute name and value and sets that attribute,
but later restores an original attribute value in a way suitable for a with statement. For example,
the following code snippet shall print Did you want to exit?:

with memento(sys, 'exit', lambda x: 'Did you want to exit?'):
    print sys.exit(1)
Compare a performance and readability with the same solution using a contextlib library.
"""
import sys


class memento(object):

    def __init__(self, obj, attr, value):
        self.obj = obj
        self.attr = attr
        self.value = value

    def __enter__(self):
        self._old_value = getattr(self.obj, self.attr)
        setattr(self.obj, self.attr, self.value)

    def __exit__(self, exc_type, exc_val, exc_tb):
        setattr(self.obj, self.attr, self._old_value)

if __name__ == "__main__":
    with memento(sys, 'exit', lambda x: 'Did you want to exit?'):
        print(sys.exit(1))