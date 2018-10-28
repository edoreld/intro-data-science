#!/usr/bin/env python3

import sys

current_url = None
current_time = 0
current_count = 0
url = None

# input comes from STDIN
for line in sys.stdin:

	# parse the input we got from mapper.py
	pair = line.split('\t')
	url = pair[0]
	time = pair[1]

	# print('{}\t{}'.format(url))
	# here time can be >1 since the mapper has performed local aggregation

	# convert time (currently a string) to int
	try:
		time = int(time)
	except ValueError:
		# time was not a number, so silently
		# ignore/discard this line
		continue

	# this IF-switch only works because Hadoop sorts map output
	# by key (here: url) before it is passed to the reducer
	# recall that no ordering is ensured by default Hadoop on the value component (here time)
	if current_url == url:
		current_time += time
		current_count += 1
		# print('Current Time: {}\n Current Count: {}', format(current_time, current_count))
	else:
		if current_url:
			# write result to STDOUT
			if current_time > 1:
				print('{}\t{}'.format(current_url, current_time / current_count))
		current_time = time
		current_url = url
		current_count = 1
		# print('Current Time: {}\nCurrent URL: {}\n Current Count: {}.', format(current_time, current_url, current_count))

# do not forget to output the last url if needed!
if current_url == url:
	print('{}\t{}'.format(current_url, current_time))
