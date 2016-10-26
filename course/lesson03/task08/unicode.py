#!/usr/bin/python3
"""
Write a function which takes a unicode string
and encodes it into a printable US-ASCII character set.
Use some real UTF-8 characters to test this function.
"""


def to_ascii(input_unicode):
    """
    Takes a unicode string and encodes it into a
    printable US-ASCII character set.

    Args:
        input_unicode(str): input unicode string

    Returns:
        str: with all characters converted to US-ASCII,
             characters that cannot be converted - will be skipped.
    """
    return input_unicode.encode("ascii", "ignore")

if __name__ == "__main__":
    print(to_ascii("ni\xf1era"))
