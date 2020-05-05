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
    try:
    	age = int(data[8].strip())
    except ValueError:
    	continue
    if age < 13:
    	print '%s\t%s' % ("under 13", 1)
    elif age > 65:
    	print '%s\t%s' % ("over 65", 1)
    else:
    	print '%s\t%s' % ("over 13 but under 65", 1)
    	

            