#!/usr/bin/python3
"""
Advanced File Copy
------------------
A task is the same as above, but a keyboard interruption shall be handled
gracefully printing a message ``Operation terminated by user``.  In order to
better visualize user interaction, file content shall be read/written line by
line with a ``time.sleep`` for one second between each line and printing a
diagnostic information like below (each dot means one line)::

    Copying a file "aaa.txt" into "bbb.txt"
    .............................
    Operation complete

In case of user initiated termination all data that was written into a file up
to data shall be preserved.

"""
import os
import time
import signal


def handler(signal, frame):
    print("Operation terminated by user", flush=True)
    exit(1)


def set_interrupt_handlers():
    signal.signal(signal.SIGINT, handler)
    signal.signal(signal.SIGTERM, handler)
    signal.signal(signal.SIGBREAK, handler)


def copy_file(in_file, out_file):
    try:
        print('Copying a file "{}" into "{}"'.format(in_file, out_file))
        with open(in_file, mode="r", encoding="utf-8") as in_fd:
            if os.path.exists(out_file):
                print("Output file already exist: {}".format(out_file))
                exit(1)

            with open(out_file, mode="w", encoding="utf-8") as out_fd:
                for line in in_fd.readline():
                    out_fd.write(line)
                    out_fd.flush()
                    print(".", end='', flush=True)
                    time.sleep(1)
                    os.kill(signal.CTRL_C_EVENT, 0)

    except KeyboardInterrupt:
        print("Operation terminated by user")
    except Exception as u_error:
        print("Cannot copy file, due to error: {}".format(u_error))
    else:
        print("Operation complete")


if __name__ == "__main__":
    set_interrupt_handlers()
    copy_file("../../alice.txt", "./alice.txt")
