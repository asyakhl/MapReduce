#!/usr/bin/env python
"""mapper.py"""

import sys

# input comes from STDIN (standard input)
infile = sys.stdin
next(infile)
for line in infile:

    line = line.strip()

    data = line.split(",")
    ip = data[0].replace(".", "").strip()

    try:
        int(ip)
    except ValueError:

        continue
    print '%s\t%s' % (ip, 1)
        
