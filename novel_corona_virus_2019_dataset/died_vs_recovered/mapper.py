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
    	died = int(data[6].strip())
        recovered = int(data[7].strip())
    except ValueError:
        continue
    
    print '%s\t%s' % ("died", died)
    print '%s\t%s' % ("recovered", recovered)
    	

            