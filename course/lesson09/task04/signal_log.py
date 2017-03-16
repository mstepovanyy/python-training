#!/usr/bin/python3
"""
Signals
-------
Write a simple program that logs all received signals to the standard input.
Every minute an application shall print a number of received signals up to data.

Besides, a ``SIGHUP`` signal shall reset a received signals counter to zero.
A ``SIGINT`` and ``SIGTERM`` signals shall terminate a program gracefully.

At exit a program shall print a total number of received signals and a number of
resets.  Use an ``atexit`` module to do this part of a task.
"""
import time
import signal
import atexit

signal_count = 0
reset_count = 0


def print_status():
    print(signal_count)


def print_signal():
    pass


def reset_signal_count():
    global signal_count
    global reset_count
    reset_count += 1
    signal_count = 0


def terminate():
    atexit.register(print_exit)
    exit(0)


def print_exit():
    print_status()
    print(reset_count)


def count_signals():
    signal.signal(signal.SIGHUP, reset_signal_count)
    signal.signal(signal.SIGINT, terminate)
    signal.signal(signal.SIGTERM, terminate)
    signal.setitimer(signal.ITIMER_REAL, -1)
    while True:
        time.sleep(1)


if __name__ == "__main__":
    count_signals()
    