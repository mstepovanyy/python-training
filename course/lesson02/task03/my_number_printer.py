#!/usr/bin/python3
"""Simplify number output for math."""

from datetime import datetime
from datetime import timedelta


class MyNumberPrinter(object):
    """
    Prints number.

    Attributes:
        number (int, float): number for printing
    """
    number = 0

    def __init__(self, number):
        self.number = number

    def me(self):
        """Prints a number itself"""
        print(self.number)

    def factorial(self):
        """Prints a factorial of a number"""
        print(self._factorial(self.number))

    def string(self, times):
        """
        Prints a string concatenated with itself number times

        Args:
            times (int): prints self.number specified number of times.
        """
        print("Some string: " + (str(self.number) + " ") * times)

    def update(self, new_value):
        """
        Modifies a number value and prints a new value

        Args:
            new_value (int, float): value that will be stored in memory.
        """
        self.number = new_value
        self.me()

    def time_in_past(self, output_format):
        """
        Accepts a one letter string that is either of s, m, h, d and
        print a time that is a number of seconds, minutes, hours, or days
        in the past since now.

        Args:
            output_format (str): format for calculations. Following values
                can be used: s - seconds, m - minutes, h - hours, d - days.
        """
        mapper = {"s": "seconds", "m": "minutes", "h": "hours", "d": "days"}
        kwargs = {mapper.get(output_format, "days"): self.number}
        print(datetime.now() - timedelta(**kwargs))

    def _factorial(self, number):
        """
        Calculates factorial, using recursion

        Args:
            number (int): number for calculation

        Returns:
            int: factorial for 'number'
        """
        if number == 1 or number == 0:
            return 1
        else:
            return self._factorial(number - 1) * number

if __name__ == "__main__":
    my_number_printer = MyNumberPrinter(23)
    my_number_printer.time_in_past("d")
    my_number_printer.factorial()
    my_number_printer.update(20)
    my_number_printer.time_in_past("s")
    my_number_printer.time_in_past("m")
    my_number_printer.time_in_past("h")
    my_number_printer.time_in_past("d")
    my_number_printer.string(10)
