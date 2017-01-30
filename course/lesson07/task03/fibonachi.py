#!/usr/bin/python3
"""
Fibonacci
---------
Write a generator which produces an infinite sequence of Fibonacci numbers.
Use it to print first 100 Fibonacci numbers followed by every tenth such number
between 100th and 1000th (e.g. 100th, 110th, 120th and so on).

.. hint::
    Use `enumerate` to solve the second part of a task.  Think of a way to form
    a finite loop off an infinite generator (e.g. use some of `itertools` module
    functions to achieve this).
"""
import itertools


def fibonacci_sequence():
    """
    Generator that returns fibonacci sequence

    Returns:
        generator(int): generator that returns integer numbers
    """
    first = 0
    second = 0
    while True:
        result = first + second
        first, second = (second, result) if result else (1, 0)
        yield result


def fibonacci(number):
    """
    Print first 100 Fibonacci numbers followed by every tenth such number
    between 100th and 'number' (e.g. 100th, 110th, 120th and so on).

    Args:
        number (int): calculate fibonacci till this number
    """
    till_number = itertools.takewhile(lambda x: x[0] < number, enumerate(fibonacci_sequence()))
    filtered = itertools.filterfalse(lambda x: x[0] > 100 and x[0] % 10, till_number)

    for index, value in filtered:
            print(value)


if __name__ == '__main__':
    fibonacci(1000)
