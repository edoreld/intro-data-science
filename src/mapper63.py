#!/usr/bin/env python3

import sys

# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    words = line.split(',')
    # increase counters



    mID = words[0]
    date = words[1]
    name = words[2]


    # ccc.it 18
    print('{}\t{}'.format(name + "," + mID + "," + date, name + "," + mID + "," + date))


