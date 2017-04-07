#!/usr/bin/python3
"""
Producer-Consumers
------------------
Write an application which spawns several children threads or processes (based
on a command line argument).  A parent shall read from a file and put all lines
into a queue.  Children shall take those lines and append them into another file
if and only if those lines start with a capital letter.  An order of lines in a
resulting file is not important, however, all lines shall be put intact.  All
threads (processes) shall exit gracefully after an input file ends and all
necessary lines are put to output an file.

Compare a performance difference between the two solutions for ``alice.txt``.

.. hint:
    Use a ``Queue.Queue`` for thread safety and ``multiprocessing.Queue`` for
    inter-process communication.
"""