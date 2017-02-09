#!/usr/bin/python3
"""
Context Manager
---------------
Redo a transaction handler task in such a way that there is no necessity to wrap
each action requiring a transaction into a separate function.

E.g. in the following code snippet there are 3 actions wrapped into a
transaction, including nested transactions:

.. code-block:: Python

    def my_func(a, b, c):
        with transaction('root'):
            print a
            with transaction('nested successful'):
                print b
            with transaction('nested with error'):
                print c
                raise Exception

.. hint::
    Use a `contextlib.context_manager` decorator to implement this task.
"""
import contextlib

transaction_count = 0


@contextlib.contextmanager
def transaction(name):
    global transaction_count
    transaction_count += 1

    local_transaction = transaction_count
    try:
        print("Transaction {} for {} started".format(local_transaction, name))
        yield
        print("Transaction {} for {} ended".format(local_transaction, name))
    except:
        print("Transaction {} for {} cancelled\n".format(local_transaction, name))


def my_func(a, b, c):
    with transaction('root'):
        print(a)
        with transaction('nested successful'):
            print(b)
        with transaction('nested with error'):
            print(c)
            raise Exception

if __name__ == '__main__':
    my_func(1, 2, 3)
