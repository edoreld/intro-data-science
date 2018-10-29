#!/usr/bin/env python3

import sys

custID = ''
name = '-'
total = '_'

# input comes from STDIN (standard input)
for line in sys.stdin:

    custID = ''
    name = '-'
    total = '-'

    # remove leading and trailing whitespace
    words = line.strip().split(',')

    if len(words) == 3:
        # Customers table
        custID = words[0]
        name = words[2]
    elif len(words) == 2:
        # Orders table
        custID = words[0]
        total = words[1]

    print('{}\t{}\t{}'.format(custID, name, total))