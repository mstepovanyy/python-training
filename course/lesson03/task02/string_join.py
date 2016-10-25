#!/usr/bin/python3
"""
Write a function that takes arbitrary number of positional
    and named arguments and returns a string in the following
    format (use only a str.join method for this):
        pos1_value, pos2_value, pos3_value
        named1=named1_value, named2=named2_value
"""


def string_convert(*args, **kwargs):
    """
    Converts passed args, and kwargs into string, in format:
        pos1_value, pos2_value, pos3_value
        named1=named1_value, named2=named2_value

    Args:
        *args: arbitrary number of arguments
        **kwargs:  arbitrary number of "key - value" arguments

    Returns:
        str: string with all *args, and **kwargs in it.
    """
    args_str = ', '.join([str(item) for item in args])
    kwargs_str = ', '.join(['='.join((key, str(value))) for key, value in kwargs.items()])
    return '\n'.join([args_str, kwargs_str])

if __name__ == "__main__":
    print(string_convert(1, 2, 3, 'a', value1="arg1", value2="arg2", value3=4))

