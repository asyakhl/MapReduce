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
    country = data[3].strip()
    state = data[2].strip()
    key = "_".join(list([country,state]))
    confirmed = int(float(data[5].strip()))
    print '%s\t%s' % (key, confirmed)

            