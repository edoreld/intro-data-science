#!/usr/bin/env python3

import sys

# input comes from STDIN
for line in sys.stdin:

    data = line.split('\t')

    fields = data[1].split(',')
    # print('{}'.format(fields))

    # print('{}'.format(fields))
    name = fields[0]
    mID = fields[1]
    date = fields[2]

    print('{}'.format(mID),end=' ')
    print('{}'.format(name), end=' ')
    print('{}'.format(date), end=' ')

