#!/usr/bin/env python3

import sys

current_cust_ID = None
current_total = 0
current_name = None

# input comes from STDIN
for line in sys.stdin:

    # 1001  SNOW GEORGE -
    # 1001 -   1285

    custID, name, total = line.rstrip('\n').split('\t')

    if total != "-":
            total = int(total)

    if not current_cust_ID:
        current_cust_ID = custID



    if current_cust_ID == custID:
        if name != "-":
            current_name = name
        if total != "-":
            current_total += total
    else:
        if current_name != '-':
            print('{}\t{}'.format(current_name, current_total))
        current_cust_ID = custID
        if total != '-':
            current_total = total
        else:
            current_total = 0
        if name != '-':
            current_name = name
        else:
            current_name = '-'

if current_name != '-':
    print('{}\t{}'.format(current_name, current_total))

    # print('{}'.format(mID),end=' ')
    # print('{}'.format(name), end=' ')
    # print('{}'.format(date), end=' ')

