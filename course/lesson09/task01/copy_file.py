#!/usr/bin/python3
"""
File Copy
---------
Write a simple program that reads content from one file an writes it to yet
another file.  All possible I/O and OS errors shall be handled gracefully (e.g.
nonexisting input file, insufficient permissions etc) and an appropriate
diagnostic information shall be printed to standard error.  If a read of an
input file fails - not subsequent write shall be done.  An output file shall be
written only if it does not exist, otherwise an error shall occur (think of
concurrency problems associated with this part of a task).

An application shall return an appropriate exit code identifying success or
failure do fulfill a requested operation.
"""
import os


def copy_file(in_file, out_file):
    try:
        with open(in_file, mode="r", encoding="utf-8") as in_fd:

            if os.path.exists(out_file):
                print("Output file already exist: {}".format(out_file))
                exit(1)

            with open(out_file, mode="w", encoding="utf-8") as out_fd:
                try:
                    for line in in_fd.readline():
                        try:
                            out_fd.write(line)
                        except IOError as w_err:
                            print("Cannot write to file {}, error: {}".format(out_file, w_err))
                except IOError as r_error:
                    print("Cannot read from file {}, error: {}".format(in_file, r_error))
    except IOError as err:
        print("Cannot open file: ({}): {}".format(type(err), err))
    except Exception as u_error:
        print("Cannot copy file, due to error: {}".format(u_error))


if __name__ == "__main__":
    copy_file("../../alice.txt", "./alice.txt")

