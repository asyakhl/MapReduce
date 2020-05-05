#!/usr/bin/env python
"""reducer.py"""

from operator import itemgetter
import sys

current_word = None
current_count = 0
current_count_afternoon=0
word = None

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    

    # parse the input we got from mapper.py
    word, count = line.split('\t', 1)

    # convert count (currently a string) to int
    try:
        count = int(count)
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue

    if int(word) == 200:
        current_count += count
    else:
        current_count_afternoon += count
            # write result to STDOUT
print '%s\t%s' % ("200", current_count)
print '%s\t%s' % ("not 200" current_count_afternoon)  


