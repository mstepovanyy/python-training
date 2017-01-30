#!/usr/bin/python3
"""
Flatten
-------
Write an iterator which takes an arbitrary number of iterables and flattens
their output (i.e. iterates over their elements returning one element from each
iterable in a loop).  For example, a return of these two iterables: ``A, B, C``,
``D, E, F`` - shall be ``A, D, B, E, C, F``.  An iterator shall end when all of
iterables are exhausted.
"""
import itertools


def flatten(*args):
    """
    Takes an arbitrary number of iterable and flattens
    their output (i.e. iterates over their elements returning one element from each
    iterable in a loop). For example, a return of these two iterables: ``A, B, C``,
    ``D, E, F`` - shall be ``A, D, B, E, C, F``.

    Args:
        args(iterable): tuple of iterables

    Returns:
        iterator: returns items from each iterable.
    """
    for values in itertools.zip_longest(*args):
        for item in values:
            if item != None:
                yield item


if __name__ == '__main__':
    print(list(flatten((1, 2, 3, 4), (5, 6), (7, 8))))

