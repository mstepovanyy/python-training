#!/usr/bin/python3
"""Prints out ASCII cat"""


class CatPrinter(object):
    """Prints out ASCII cat, with using 4 different string literals"""

    top = r'_-_-_-_-_-_-_'
    bottom = """'"'"'"'"'"'"'"""
    content_top = ("|  ^_____^  |\n"
                   "/  (.) (.)  \\\n"
                   "|  ( t   )  |  Miaowww")
    content_bottom = ('''\    ==/    /\n'''
                      '''|           |''')

    def print(self):
        """Prints out ASCII cat"""
        print(self.top)
        print(self.content_top)
        print(self.content_bottom)
        print(self.bottom)

if __name__ == "__main__":
    cat = CatPrinter()
    cat.print()
