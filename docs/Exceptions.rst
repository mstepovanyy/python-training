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
    
    This function prints out a given traceback and exception to sys.stderr.
    When an exception is raised and uncaught, the interpreter calls sys.excepthook with three arguments, the exception class, exception instance, and a traceback object. In an interactive session this happens just before control is returned to the prompt; in a Python program this happens just before the program exits. The handling of such top-level exceptions can be customized by assigning another three-argument function to sys.excepthook.


