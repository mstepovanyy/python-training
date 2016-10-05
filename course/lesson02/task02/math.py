#!/usr/bin/python3
"""Example of math module

This module uses to calculate factorial and harmonic medium value
"""


def factorial(a):
    """Accepts one integer and prints its factorial (recursive)"""
    if a == 1 or a == 0:
        return 1
    else:
        return factorial(a - 1) * a


def my_args(*args):
    """Accepts an arbitrary number of arguments and prints them all"""
    for item in args:
        print(item)
    print("In one line: " + str(args))


def harmony(*args):
    """
    Takes an arbitrary number of floats and prints their harmonic
    medium value. Calculation is done with formula:
      number_of_args \ (1 \ item1 + 1 \ item2 + ...)

    Args:
          *args (tuple): number of arguments with a type: float, integer

    Returns:
        float: harmonic medium value
    """
    result = 0
    if 0 in args:
        return 0.0

    for item in args:
        result += 1 / item

    return len(args) / result


if __name__ == "__main__":
    # tests for factorial
    assert factorial(5) == 120
    assert factorial(1) == 1
    assert factorial(0) == 1
    assert factorial(2) == 2
    assert factorial(16) == 20922789888000

    # tests for args
    my_args(1, 2, "this", "is", "args")

    # tests for harmony
    print(harmony(1.0))
    print(harmony(1.0, 5.0, 0.0))
    print(harmony(1.0, 5.0))
    print(harmony(1.0, 5.0, 0))

