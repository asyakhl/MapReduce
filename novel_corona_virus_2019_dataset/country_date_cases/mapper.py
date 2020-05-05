#!/usr/bin/env python
"""mapper.py"""

import sys
from datetime import datetime
# input comes from STDIN (standard input)
infile = sys.stdin
next(infile)
for line in infile:
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    data = line.split(",")
    country = data[3].strip()
    date = data[1].strip()
    date = datetime.strptime(date, "%d/%m/%y")
    date = datetime.strftime(date, "%d:%m:%y")
    key = "_".join(list([country,date]))
    confirmed = int(data[5])
    print '%s\t%s' % (key, confirmed)

            