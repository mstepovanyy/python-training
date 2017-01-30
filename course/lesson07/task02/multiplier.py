#!/usr/bin/python3
"""
Multiplier
----------
Create a function returning a list of all numbers ``N`` smaller than input
integer ``M`` such that ``N`` is a multiplier of ``3`` while ``N + 1`` is a
multiplier of ``5``.  Use it to print all such numbers smaller than ``100``.

.. hint::
    Use an `xrange` function and a list comprehension to solve this task.
"""


def multiplier(to):
    """
    Returns list of numbers that is multiplier of 3, and "N + 1" is a multiplier of 5

    Args:
        to (int): maximum value

    Returns:
        list(int): returns list of numbers
    """
    return [i for i in range(to) if i % 3 == 0 and (i + 1) % 5 == 0]


if __name__ == '__main__':
    print("Range of numbers: {}".format(multiplier(50)))
