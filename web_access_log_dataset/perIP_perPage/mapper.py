#!/usr/bin/env python
"""mapper.py"""

import sys

# input comes from STDIN (standard input)
infile = sys.stdin
next(infile)
for line in infile:

    line = line.strip()

    data = line.split(",")
    ip = data[0].replace(".", "").strip()
    webpage = data[2].partition("/")[2].strip()

    try:
        int(ip)
    except ValueError:
    	continue

    ip_page = "_".join(list([ip, webpage]))
    print '%s\t%s' % (ip_page, 1)
        
