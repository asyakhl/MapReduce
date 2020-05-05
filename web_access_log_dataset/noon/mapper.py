#!/usr/bin/env python
"""mapper.py"""

import sys

# input comes from STDIN (standard input)
infile = sys.stdin
next(infile)
for line in infile:

    line = line.strip()

    data = line.split(",")
    time = data[1][13:].replace(":","")

    try:
        int(time)
    except ValueError:

        continue
    print '%s\t%s' % (time, 1)
        
