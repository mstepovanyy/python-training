#!/usr/bin/python3
"""
2.4   Custom Dictionary

Write a function which returns a custom dictionary class
which allows to set a predefined set of custom attributes
(but not an arbitrary attribute).

E.g. the following code snippet shall work just fine:

Test = dict_with_attrs('test', 'other')
d = Test({'a': 1}, test='test')
d.other = 'Hey!'
d[10] = 11

# This shall fails:
d.unknown = 42
"""


class Test(dict):
    attributes = ()

    def __init__(self, dictionary, **kwargs):
        super().__init__(dictionary)
        for key, value in kwargs.items():
            self.__dict__[key] = value

    def __getattr__(self, item):
        if item in self.attributes:
            return self.__dict__.get(item)
        else:
            return self.__dict__[item]

    def __setattr__(self, key, value):
        if key in self.attributes:
            self.__dict__[key] = value
        else:
            raise AttributeError("No attribute found for: {}".format(key))


def dict_with_attrs(*args):
    Test.attributes = args
    return Test


if __name__ == "__main__":
    Test = dict_with_attrs('test', 'other')
    d = Test({'a': 1}, test='test')
    d.other = 'Hey!'
    d[10] = 11

    # This shall fails:
    d.unknown = 42