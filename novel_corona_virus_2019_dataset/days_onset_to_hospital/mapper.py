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
    	hosp_visit = data[11].strip()
        hosp_visit = datetime.strptime(hosp_visit, "%m/%d/%y")
        onset = data[9].strip()
        onset = datetime.strptime(onset, "%m/%d/%y")
        country = data[6].strip()
        days = (hosp_visit-onset).days
        print '%s\t%s' % (country, days)
    except ValueError:
    	continue
    
    
    	

            