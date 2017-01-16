#!/usr/bin/python3
"""
Using a `timeit` module compare a speed of ``1 000 000`` operations of creating
a `tuple`, a `list`, and a `set` of all integer digits (numbers ``0-9``).
"""
import timeit

if __name__ == '__main__':
    print(timeit.timeit("tuple()", number=1000000))
    print(timeit.timeit("list()", number=1000000))
    print(timeit.timeit("{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}", number=1000000))
