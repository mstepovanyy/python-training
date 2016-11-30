#!/usr/bin/python3
"""
Write a program that prints some statistics
about itself to standard output: a path to executable,
command line arguments, imported module names
and corresponding file paths, environment variables.
"""
import sys
import os
import types


def statistic():
    """Prints statistics about itself"""
    stat_str = \
        "\nPath: " + sys.argv[0] + \
        "\nArgs: " + ", ".join(sys.argv[1: -1]) + \
        "\nModules: \n\t" + \
        "\n\t".join(": ".join(item) for item in humanize(get_modules())) + \
        "\n ENV: \n\t" + \
        "\n\t".join(": ".join(item) for item in os.environ.items())
    print(stat_str)


def get_modules():
    """Returns list of imported modules"""
    return [item for item in globals().values() if isinstance(item, types.ModuleType)]


def humanize(modules):
    """Returns generator with tuple (module.__name__, module.__file__)"""
    for item in modules:
        yield (item.__name__, item.__file__ if "__file__" in dir(item) else "builtin")

if __name__ == "__main__":
    statistic()
