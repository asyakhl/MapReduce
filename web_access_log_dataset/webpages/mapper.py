#!/usr/bin/env python
"""mapper.py"""

import sys

# input comes from STDIN (standard input)
infile = sys.stdin
next(infile)
for line in infile:
   
    line = line.strip()
    
    data = line.split(",")
   
    webpage = data[2].partition("/")[2].strip()
    
    if "HTTP" not in webpage:
        continue
    else:
        print '%s\t%s' % (webpage, 1)


