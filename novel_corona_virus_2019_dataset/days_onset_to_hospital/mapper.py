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
    	hosp_visit = data[11].strip()
        hosp_visit = datetime.strptime(hospital_visit, "%m/%d/%y")
        onset = data[9].strip()
        onset = datetime.strptime(onset, "%m/%d/%y")
    except ValueError:
    	continue
    country = data[6].strip()
    days = str(hosp_visit-onset).split(",")[0]
    print '%s\t%s' % (country, days)
    
    	

            