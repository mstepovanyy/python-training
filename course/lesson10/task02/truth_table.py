#!/usr/bin/python3
"""
Write a Mixin class that checks if a given class instance instance is True or False based on a truth table.
A truth table is a list of object hashes that would evaluate to True (or False) specified as a class attribute.
For example, the following code snippet shall print True True:

class TrueTest(int, TruthTable):

    __true_values__ = (0, 1, 2, 3)

class FalseTest(str, TruthTable):

    __false_values__ = ('false', hash('no'))

print bool(TrueTest(0)), bool(FalseTest(''))
"""


class TruthTable(object):

    def __init__(self, value):
        if hasattr(self, "__true_values__"):
            self.value = value in self.__true_values__
        if hasattr(self, "__false_values__"):
            self.value = not (value in self.__false_values__ or hash(value) in self.__false_values__)

    def __bool__(self):
        return self.value

    def __int__(self):
        return self.value

    def __repr__(self, other):
        return True

    def __call__(self):
        return True


class TrueTest(TruthTable, int):

    __true_values__ = (0, 1, 2, 3)


class FalseTest(str, TruthTable):

    __false_values__ = ('false', hash('no'))

if __name__ == "__main__":
    print("{} {} {}".format(bool(TrueTest(0)), bool(FalseTest('')), bool(FalseTest('no'))))