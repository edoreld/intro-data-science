#!/usr/bin/env python3

import sys

for line in sys.stdin:

    data = line.split('\t')
    print('{}'.format(data[0]))