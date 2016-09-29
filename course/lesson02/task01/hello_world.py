#!/usr/bin/python3
"""This is module for lesson 02, task 01

Module prints ``Hello World`` and a current time.
"""

from datetime import date


class HelloWorld(object):
    """This class responsible for printing hello message, and current date."""

    def __init__(self):
        """Initialize hello message for class object."""
        self.hello_str = 'Hello World'

    def say_hello(self):
        """Prints message, that is defined in hello_str"""
        print(self.hello_str)

    def say_date(self):
        """Prints current date in iso format"""
        print("Current date: " + date.today().isoformat())

if __name__ == "__main__":
    obj = HelloWorld()
    obj.say_hello()
    obj.say_date()
