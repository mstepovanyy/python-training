#!/usr/bin/python3
"""
File Copy
---------
Implement a parametrized file copy operation accepting the following arguments:

    - `input file path`: specified as either first argument, or through one of
      ``-i, --input`` options, required;

    - `output file path`: specified as either second argument, or through one of
      ``-o, --output`` options, required;

    - `buffer size in bytes`: specified as one of ``-s, --buffer-size`` options,
      optional, defaults to ``8192``;

    - `program help`: specified as one of ``-h, --help`` option;  an application
      shall print a program help and exit if this option is specified;

    - `verbose mode`: specified as one of ``-v, --verbose`` options, optional,
      defaults to ``False``;  an application shall print a dot per each file
      chunk copy in this mode;

In case of any argument error an application shall print an appropriate error
and a short usage information (not help).  Any other error shall be handled
gracefully.  An application shall return an appropriate exit code.
"""

import argparse

def parse():
    parser = argparse.ArgumentParser(description="File Copy")
    parser.add_argument("-i", "--input", dest="in_")
    parser.add_argument("-o", "--output", dest="out_")
    parser.add_argument("input_file_path", nargs="?")
    parser.add_argument("output_file_path", nargs="?")

    parser.add_argument("-s", "--buffer-size", default=8192, type=int)
    parser.add_argument("-v", "--verbose", default=False)

    print(parser.parse_args("input.txt output.txt".split()))
    print(parser.parse_args("-ooutput.txt -iinput.txt".split()))
    print(parser.parse_args("-o output.txt -s 8192 input.txt".split()))
    print(parser.parse_args("--input input.txt output.txt --buffer-size=8192".split()))

if __name__ == "__main__":
    parse()
