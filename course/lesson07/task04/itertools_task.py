#!/usr/bin/python3
"""
Itertools
---------
Using `itertools` write an function returning an iterator over the following
tuples of numbers:

    - the first number shall be equal to the first function argument;
    - the second number shall start with the second function argument and
      increase by the first function argument after each turn;
    - the third number shall loop between the first and the third argument
      forth and back several times that is equal to the second argument;

For example, the following call ``func(1, 2, 3)`` shall have the following
output::
    1, 2, 1
    1, 3, 2
    1, 4, 3
    1, 5, 2
    1, 6, 1
    1, 7, 2
    1, 8, 3
    1, 9, 2
    1, 10, 1
"""
import itertools


def func(first, second, third):
    """
    Returns an iterator over the following
    tuples of numbers:

    - the first number shall be equal to the first function argument;
    - the second number shall start with the second function argument and
      increase by the first function argument after each turn;
    - the third number shall loop between the first and the third argument
      forth and back several times that is equal to the second argument;

    Args:
        first (int)
        second (int)
        third (int)

    Returns:
        infinite iterator.
    """
    third_value = itertools.cycle(itertools.chain(range(first, third + 1), reversed(range(first+1, third))))
    return zip(itertools.repeat(first), itertools.count(second), third_value)


if __name__ == '__main__':
    print("output::")
    for item in list(itertools.islice(func(1, 2, 3), 9)):
        print("\t{}, {}, {}".format(*item))
