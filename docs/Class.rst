*****
Class
*****

.. contents

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


