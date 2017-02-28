#!/usr/bin/python3
"""
2.3   Timer

Write a program that waits for a user input and prints a dot every second
until a user either hit Enter or is killed with a signal.
In case of a Ctrl-C a message User input cancelled shall be printed
on a new line. If a user input was received an application shall print it back on a new line.

Hint

Use a system timer to implement this task without threads.
"""
import signal


def print_second():
    print(".", end="", flush=True)


def user_exit():
    print("User input cancelled")
    exit(1)


def wait_for_input():
    signal.signal(signal.SIGALRM, print_second)
    signal.signal(signal.SIGTERM, user_exit)
    signal.setitimer(signal.ITIMER_REAL, -1)

    out = input("user input:")
    print(out)


if __name__ == "__main__":
    wait_for_input()