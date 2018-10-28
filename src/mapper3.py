#!/usr/bin/env python3
 
import sys
from itertools import groupby
 
# input comes from STDIN (standard input)

dict ={}

for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    words = line.split()
    # increase counters
    for word in words:
        if word not in dict:
            dict[word] = 1
        else:
            dict[word] = dict[word] + 1

for word, value in dict.items():
    print('{}\t{}'.format(word, value))

