#!/usr/bin/python3
"""
Fork
----
Write an application which recursively forks itself until a recursion depth
reaches a specified value (passed as a command-line argument).  Each child
application shall print its process ID on start and exit;  each parent
application shall print a child process ID it has forked and wait for its
completion.  Below is an example log of an application stack::

    Task 1 pid 1234 started
    Task 1 pid 1234 spawned child 1238
    Task 2 pid 1238 started
    Task 3 pid 1251 started
    Task 2 pid 1238 spawned child 1251
    Task 3 pid 1251 complete
    Task 2 pid 1238 complete
    Task 1 pid 1234 complete

Note that it is OK if a log messages from a parent and a child go out of sync.
"""

import argparse
import sys
import os
import time


def fork_example(number):
    if number <= 1:
        return
    else:
        start_process()
        fork_example(number - 1)


def start_process():
    pid = os.fork()
    if pid == 0:
        print("Pid {} started".format(os.getpid()))
        time.sleep(1)
        print("Pid {} completed".format(os.getpid()))


if __name__ == "__main__":
    parser = argparse.ArgumentParser("Fork example")
    parser.add_argument("-n", "--number", dest="number", type=int)
    args = parser.parse_args(sys.argv[1:])
    fork_example(args.number)