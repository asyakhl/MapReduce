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
    if data[1].strip() == "negative":
    	time = data[12].strip().split("  ")
    	time = time[1].strip()
    	am_pm_time = datetime.strptime(time, "%I:%M:%S %p")
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

            