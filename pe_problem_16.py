#! /usr/bin/python
# -*- coding: utf-8 -*-
#
##
##   Power digit sum
##   Problem 16
##
##   2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
##
##  What is the sum of the digits of the number 2^1000?

import time
import math

results = 1
print "Let's do the slow one."
start_time = time.time()

for count in range (0, 1000):
  results *= 2
print("------%s seconds ----" % (time.time() - start_time))

print (str(results))

print "Let's use the built-in function"
start_time = time.time()
results = 2**1000
print("------%s seconds ----" % (time.time() - start_time))
print (str(results))

final_value = 0
my_long_string = str(results)
for count in range(0,len(my_long_string)):
  final_value += int(my_long_string[count])

print final_value
