#! /usr/bin/python
# -*- coding: utf-8 -*-
#
#  Amicable numbers
#  Problem 21
#
#  Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
#  If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.
#
# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. 
# The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
#
# Evaluate the sum of all the amicable numbers under 10000.
#
# btw, amicable numbers should not contain the numbers themselves
# so 3,4 is not an amicable number
# and 220,284 is the smallest amicable numbers

import math
divisors = []
amicable_pairs=[]

def is_prime(n):
  if (n<13):
    for i in range(2, n):
      if n%i == 0:
        return False
    return True
  else:
    maxval = int(math.sqrt(n))
    for i in range(2, maxval + 1):
      if n%i == 0:
        return False
        break
    return True


def check_for_divisors(s1, s2, num):
  global divisors
  outloop = len(s1)
  for n in range (0, outloop):
    for value in s1:
      newvalue = s1[n] * value
      if ((newvalue not in s2) and (newvalue < num) and (num % newvalue == 0)):
        s2.append(newvalue)
  for value in s2:
    if value not in divisors:
      divisors.append(value)


def check_for_term(num):
  global divisors
  base = []
  set1 = []
  set2 = []
  done = False
  base.append(1) ## all number divisible by 1
  for count in range(1,(num+1)/2):
    if ((num % count == 0)):
      base.append(count)
  ## Check for divisible term and shit
  check_for_divisors(base,base,num)
  ## check_for_divisors(base,base,num)



for count in range(1, 10000):
  if(is_prime(count)):
    ## skip, save some speed
    continue
  else:
    divisors[:] = []
    sum_of_divisors = 0
    sum_of_divisors2 = 0
    check_for_term(count)
    divisors.sort()
    ## print count, divisors,
    ## add the divisors together
    for item in divisors:
      sum_of_divisors += item
    divisors[:] = []
    check_for_term(sum_of_divisors)
    divisors.sort()
    ## print sum_of_divisors,
    ## print divisors,
    ## add the divisors 2 together
    for item in divisors:
      sum_of_divisors2 += item
    ## print sum_of_divisors2
    if (sum_of_divisors != count) and (sum_of_divisors2 == count):
      print ("amicable pairs found " + str(count) + "  " + str(sum_of_divisors))
      amicable_pairs.append(count)

print amicable_pairs

sum_of_amicable_pairs = 0
for item in amicable_pairs:
  sum_of_amicable_pairs += item
print sum_of_amicable_pairs
