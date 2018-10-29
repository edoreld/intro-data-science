#!/usr/bin/env python3

# 01\t1

import sys

dic = {}

for line in sys.stdin:
	data = line.split('\t');
	month = data[0]

	if (month not in dic):
		dic[month] = 1
	else:
		dic[month] = dic[month] + 1

for key, value in dic.items():
	print('{}\t{}'.format(key, value))