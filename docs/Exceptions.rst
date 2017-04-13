**********
Exceptions
**********

.. content::

.. sectnum::


Hierarchy
=========

* SystemExit
* KeyboardInterrupt
* GeneratorException
* Exception

    * StopIteration
    * StopAsyncIteration
    * ArithmeticError
    * ...


Try catch structure
===================

.. code-block:: Python

    >>> def divide(x, y):
    ...     try:
    ...         result = x / y
    ...     except ZeroDivisionError:
    ...         print("Exception cached")
    ...     else:
    ...         print("No exceptions raised")
    ...     finally:
    ...         print("Runs every time")


Unhandled Exceptions
====================

It is possible to define handler, for any uncought exception.
.. note::
    sys.excepthook(type, value, traceback)
    
    This function prints out a given traceback and exception to sys.stderr. When an exception is raised and uncaught,
    the interpreter calls sys.excepthook with three arguments, the exception class, exception instance,
    and a traceback object. In an interactive session this happens just before control is returned to the prompt;
    in a Python program this happens just before the program exits. The handling of such top-level exceptions can be
    customized by assigning another three-argument function to sys.excepthook.


Asynchronous events
===================

Very limited on Windows.
This module provides mechanisms to use signal handlers in Python.
A common sense is to handle at least `SIGINT` and `SIGTERM` gracefully.

mudule signal_ - Set handlers for asynchronous events

.. _signal: https://docs.python.org/3/library/signal.html
.. _atexit: https://docs.python.org/3/library/atexit.html

module atexit_ - register exit handlers
.. note::
    The functions registered via this module are not called when the program is killed
    by a signal not handled by Python, when a Python fatal internal error is detected, or when os._exit() is called.


