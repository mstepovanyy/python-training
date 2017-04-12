*****
Class
*****

.. contents::

.. sectnum::

Class Attributes vs Object attributes
=====================================

It is possible to read class attributes' values from a class instance, but it is allowed to write and delete instance attributes only.

.. code-block:: Python

    >>> class A(object):
    ...   class_attr = 1
    ...
    >>> b = A()
    >>> b.obj_attr = 2
    >>> b.class_attr
    1
    >>> b.obj_attr
    2
    >>> A.class_attr = 3
    >>> b.class_attr
    3
    >>> b.class_attr = 4
    >>> A.class_attr
    3
    >>> b.class_attr
    4

`__slots__`
===========

Used to save space, by skipping `__dict__` in each object. 

By default, instances of both old and new-style classes have a dictionary for attribute storage. This wastes space for objects having very few instance variables. The space consumption can become acute when creating large numbers of instances.
The default can be overridden by defining __slots__ in a new-style class definition. The __slots__ declaration takes a sequence of instance variables and reserves just enough space in each instance to hold a value for each variable. Space is saved because __dict__ is not created for each instance.

Class method
============
A class method is a method which receives a class itself as the first argument instead of a class instance.

Static method
=============
A static method is a method that receives neither a class nor a class instance as the first argument. It is accessible through a declaring class only.

Magic Methods
=============

This methods compiled statically(not in run time). So this methods cannot be overrided at run-time.

`__new__`
+++++++++

1. Control creation of class
2. Used in case of subclassing immutable type(int, float, complex, str, tuple, frozenset, bytes)
3. Returns created object, so can be used in Factory, Singleton pattern.

`__init__`
++++++++++
1. Responcible for initialization of created object.



