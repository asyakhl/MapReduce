#!/usr/bin/env python
"""mapper.py"""

import sys
import csv
import re
from datetime import datetime
# input comes from STDIN (standard input)
infile = sys.stdin
next(infile)
for line in csv.reader(iter(infile)):
    data = line
    if data[1].strip() == "negative":
    	time = re.split(" |  ", data[12].strip())
    	time = time[1].strip()
    	am_pm_time = datetime.strptime(time, "%H:%M:%S")
    	twenty_four_hour_time = datetime.strftime(am_pm_time, "%H:%M:%S")
    	time = int(twenty_four_hour_time.replace(":", ""))
    else:
    	continue
    if time < 120000: 
    	print '%s\t%s' % ("Morning", 1)
    elif 120000 < time < 200000:
    	print '%s\t%s' % ("Mid-day", 1)
    else:
    	print '%s\t%s' % ("Night", 1)

            