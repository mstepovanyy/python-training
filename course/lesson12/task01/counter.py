#!/usr/bin/python3
"""
Counter
-------
Spawn several `counter` threads each counting from ``1`` to a specified number
and printing those numbers to the standard output.  Each `counter` thread shall
sleep for a specified number of seconds (float) between prints.  There shall be
a `status` thread which prints how many threads are still alive in a specified
time interval.  An application shall exit when all `counter` threads finish
their work.
"""

import threading
import sys
import time


class MyThread(threading.Thread):
    counter = 1
    delay = 0
    retries = 0

    def __init__(self, delay, retries):
        super().__init__()
        self.delay = delay
        self.retries = retries

    def run(self):
        while self.counter < self.retries:
            print(self.counter, file=sys.stdout)
            self.counter += 1
            time.sleep(self.delay)


def start_threads():
    MyThread(0.6, 4).start()
    MyThread(0.2, 10).start()

    while threading.active_count() != 1:
        print("Active Threads: {}".format(threading.active_count()))
        time.sleep(1)

    print("END")

if __name__ == "__main__":
    start_threads()

