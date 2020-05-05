#!/usr/bin/env python
"""mapper.py"""

import sys
import csv
# input comes from STDIN (standard input)
infile = sys.stdin
next(infile)
for line in csv.reader(iter(infile)):
    data = line
    try:
        died = int(float(data[6].strip()))
        recovered = int(float(data[7].strip()))
    except ValueError:
        continue
    
    print '%s\t%s' % ("died", died)
    print '%s\t%s' % ("recovered", recovered)
    	

            