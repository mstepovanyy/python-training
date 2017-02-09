#!/usr/bin/python3
"""
Transaction Manager
-------------------
Write a simple decorator which implements a transaction handler.  There shall be
no real transaction performed, instead, a decorator shall print messages like
``Transaction 1 for my_func started``, ``Transaction 2 for my_func complete``,
or ``Transaction 3 for my_func cancelled`` at transaction start, completion, or
cancellation (in case of an error in a decorated function) accordingly.

Declare several functions doing different stuff that are decorated with this
decorator.

.. hint::
    For simplicity it is allowed to use a global variable to auto-increment
    transaction numbers.  Use a __name__ function attribute to distinguish
    transactions for different functions.
"""


transaction_count = 0


def transactions(func):
    """Decorator that counts transactions."""
    def wrapper(*args, **kwargs):
        global transaction_count
        transaction_count += 1
        print("Transaction {} for {} started".format(transaction_count, func.__name__))
        try:
            result = func(*args, **kwargs)
            print("Transaction {} for {} complete\n".format(transaction_count, func.__name__))
            return result
        except Exception as e:
            print("Transaction {} for {} cancelled\n".format(transaction_count, func.__name__))

    return wrapper


@transactions
def throw_error():
    """Function that throws error"""
    raise TimeoutError()


@transactions
def print_hello():
    """Function without args, print hello message"""
    print("Hi there...")


@transactions
def print_hello_to(name):
    """Function with arguments, print hello message"""
    print("Hello {}.".format(name))


if __name__ == "__main__":
    throw_error()
    print_hello()
    print_hello_to("Me")



