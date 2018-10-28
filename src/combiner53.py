#!/usr/bin/env python3

import sys

dictionnaire = {}
for line in sys.stdin:
	data = line.split('\t');
	if (data[0] not in dictionnaire):
		dictionnaire[data[0]] = data[1]

for key, value in dictionnaire.items():
	print('{}\t{}'.format(key, value), end='')