#!/usr/bin/python3
"""
2.5   Proxy

Write a universal transparent proxy that is able to provide read/write access to attributes
of any object instance being proxied. For example, the following code snippet shall print Hello World!:

class A(object):

    phrase = 'Test'

    def test(self):
        print self.phrase

proxy = Proxy(A())
proxy.phrase = 'Hello World!'
proxy.test()
In addition, a proxy shall count how many times a proxied object methods were called (separately for each method).

Note

A method can be accessed but not called, hence, you need to proxy method objects as well to fulfill this task.
At the same moment, any read/write operation on method proxy shall be delegated to an original method as well.
"""


def __wrapper__(fn, callback, name):
    def function(*args, **kwargs):
        callback(name)
        return fn(*args, **kwargs)
    return function


class Proxy(object):

    def __init__(self, cls):
        self.__dict__["__cls__"] = cls
        self.__dict__["__no_calls__"] = {}

    def __setattr__(self, key, value):
        if key in self.__dict__:
            self.__dict__[key] = value
        else:
            setattr(self.__cls__, key, value)

    def __getattr__(self, item):
        """
        Override each method of input class with wrapped object
        """
        attr = getattr(self.__cls__, item)
        if hasattr(attr, "__call__"):
            return __wrapper__(attr, self.__call_back__, item)

        return getattr(self.__cls__, item)

    def __call_back__(self, name):
        """
        Count number of calls,
        running just before direct call to object
        """
        self.__dict__["__no_calls__"][name] = self.__dict__["__no_calls__"].get(name, 0) + 1

    def __del__(self):
        """
        At exit outputs summary for proxy
        """
        print("Number of calls:")
        for key, value in self.__dict__["__no_calls__"].items():
            print("\t{}: {}".format(key, value))

if __name__ == "__main__":
    class A(object):
        phrase = 'Test'

        def test(self):
            print(self.phrase)

    proxy = Proxy(A())
    proxy.phrase = 'Hello World!'
    proxy.test()
    proxy.test

