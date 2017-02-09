#!/usr/bin/python3
"""
Method Generator
----------------
Write a decorator which generates a set of methods in a class given a template
function and a dictionary of function names and their parameters.

E.g. the following two code snippets shall be equivalent:

.. code-block:: Python

    def template(self, a, b, c):
        print self.x, a, b, c

    method_table = {
        'test': dict(a=10, c=20),
        'other_test': dict(b=30),
    }

    @template_methods(template, method_table):
    class A(object):
        x = 10
        pass

.. code-block:: Python

    class A(object):
        x = 10

        def test(self, b):
            print self.x, 10, b, 30

        def other_test(self, a, c):
            print self.x, a, 20, c

.. hint::
    You might use a `funcutils.partial` to make this task easier.
"""
import functools


def template(self, a, b, c):
    print(self.x, a, b, c)


method_table = {
    'test': dict(a=10, c=20),
    'other_test': dict(b=30),
    'first_test': dict(a=2),
}


class template_methods:
    """
    Decorator that generates class methods, based on template,
    and arguments provided in dictionaty
    """
    def __init__(self, template, method_table):
        """
        Args:
            template (func): class method that will be called
            method_table (dict): method names, with arguments.
        """
        self.template = template
        self.method_table = method_table

    def __call__(self, origin_class):
        template_args = template.__code__.co_varnames[1:]

        for name, data in self.method_table.items():
            args = list()
            kwargs = dict()
            put_in_args = True
            for item in template_args:
                if item in data and put_in_args:
                    args.append(data[item])
                elif item in data:
                    kwargs[item] = data[item]
                else:
                    put_in_args = False

            if len(data) == 1 and 'b' in data.keys():
                # this is special case due to partial method functionality.
                setattr(origin_class, name, lambda self, a, c: template(self, a, data['b'], c))
            else:
                setattr(origin_class, name, functools.partialmethod(template, *args, **kwargs))

        return origin_class



@template_methods(template, method_table)
class A(object):
    x = 10
    pass

if __name__ == '__main__':
    a = A()
    a.test(3)
    a.other_test(2, 3)
    a.first_test(1, 4)

