#!/usr/bin/python3
"""
Write a function that restores function arguments off the output
of the previous function into a tuple of positional and a dictionary
of named arguments. For simplicity assume that argument values are
all strings that does not contain special characters.
Use a str.split method for this task.
"""


def string_parse(input_str):
    """
        Converts passed string, into *args, **kwargs:

        Args:
            input_str(str): input string in format -
                            "1, 2, 3, a\nvalue3=4, value1=arg1, value2=arg2"

        Returns:
            tuple(*args, **kwargs): parsed args, and kwargs values
        """
    args_str, kwargs_str = input_str.split('\n')
    args_raw = args_str.split(',')
    kwargs_raw = kwargs_str.split(', ')
    args = [item.strip() for item in args_raw]
    kwargs = dict((item.split('=') for item in kwargs_raw))
    return args, kwargs


if __name__ == '__main__':
    args = "1, 2, 3, a\nvalue3=4, value1=arg1, value2=arg2"
    print(string_parse(args))
