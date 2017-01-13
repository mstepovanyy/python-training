#!/usr/bin/python3
"""
Replace each occurence of ``Alice was`` to ``Alice is`` and print a number of
modified phrases;  sentences breaking though lines shall be modified correctly
as well.
"""
import re
from course.lesson05.task01.task01 import get_output_file


def replace_in_file(file_name):
    """
    Replace each occurence of ``Alice was`` to ``Alice is``, and returns number of changes

    Args:
        file_name (str): path to file

    Returns:
         int : number of changes in file
    """

    with open(file_name, mode='r', encoding='utf-8') as fd_in:
        with open(get_output_file(file_name), mode='w', encoding='utf-8') as fd_out:
            file_content, count = re.subn(r'Alice(\s*)was', 'Alice is', fd_in.read())
            fd_out.write(file_content)

    return count

if __name__ == '__main__':
    print('Number of changes in file: {}'.format(replace_in_file('../../alice.txt')))
