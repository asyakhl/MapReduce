#!/usr/bin/env python
"""mapper.py"""

import sys
import csv
from datetime import datetime
# input comes from STDIN (standard input)
infile = sys.stdin
next(infile)
for line in csv.reader(iter(infile)):

    data = line
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
    	

            