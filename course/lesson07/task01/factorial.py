#!/usr/bin/python3
"""
Factorial
---------
Write a non-recursive function calculating a factorial of a number using an
`xrange` function.
"""


def factorial(number):
    """
    Calculates factorial for specified number

    Args:
        number (int): calculate factorial for this value

    Returns:
        int: factorial for provided value
    """
    result = 1
    for item in range(1, number + 1):
        result *= item
    return result

if __name__ == "__main__":
    print(factorial(0))
    print(factorial(1))
    print(factorial(2))
    print(factorial(3))
    print(factorial(4))
    print(factorial(6))
    print(factorial(9))

