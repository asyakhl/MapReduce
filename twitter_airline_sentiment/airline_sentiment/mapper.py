#!/usr/bin/env python
"""mapper.py"""

import sys

# input comes from STDIN (standard input)
infile = sys.stdin
next(infile)
for line in infile:
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    data = line.split(",")
    airline = data[5].strip()
    sentiment = data[1].strip()
    word = "_".join(list([airline, sentiment]))
    print '%s\t%s' % (word, 1)
            