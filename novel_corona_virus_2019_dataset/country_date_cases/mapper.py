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
    date = data[1].strip()
    date = datetime.strptime(date, "%m/%d/%Y")
    date = datetime.strftime(date, "%m:%d:%Y")
    key = "_".join(list([country,date]))
    confirmed = int(float(data[5]))
    print '%s\t%s' % (key, confirmed)

            