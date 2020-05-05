#!/usr/bin/env python
"""mapper.py"""

import sys
import csv

# input comes from STDIN (standard input)
infile = sys.stdin
next(infile)
for line in csv.reader(iter(infile)):
    data = line
    if len(data) > 6:
        airline = data[5].strip()
        sentiment = data[1].strip()
        word = "_".join(list([airline, sentiment]))
        print '%s\t%s' % (word, 1)
    else:
	    next(infile)