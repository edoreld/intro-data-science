#!/usr/bin/env python3

import sys

dict ={}

for line in sys.stdin:
    # remove leading and trailing whitespace and split the line by comma
    data = line.strip().split(',')

    if (int(data[1]) <= 1000):
        continue

    print('{}\t{}'.format(data[0], data[1]))