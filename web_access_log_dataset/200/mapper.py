#!/usr/bin/env python
"""mapper.py"""

import sys

# input comes from STDIN (standard input)
infile = sys.stdin
next(infile)
for line in infile:

    line = line.strip()

    data = line.split(",")
    status = data[3].strip()

    try:
        int(status)
    except ValueError:

        continue
    print '%s\t%s' % (status, 1)
        
