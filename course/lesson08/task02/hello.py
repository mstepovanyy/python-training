#!/usr/bin/python3
"""
Hello World
-----------
Write a simple parametrized decorator so that the below code snippet prints
``Hello\nWorld`` to the standard output:

.. code-block:: Python

    @decorator('World')
    def function(arg):
        print arg

    function('Hello')
"""


def decorator(name):
    """decorator with arguments"""
    def wrapper_fn(func):
        def wrapper(hello):
            func("{}\n{}".format(hello, name))
        return wrapper
    return wrapper_fn


@decorator('World')
def function(arg):
    """Print data to output"""
    print(arg)


if __name__ == '__main__':
    function('Hello')
