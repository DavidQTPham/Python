#! /usr/bin/python
# -*- coding: utf-8 -*-
##   Non-abundant sums
##   Problem 23
##
##   A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. 
##   For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.
##
##   A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.
## 
##   As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, 
##   the smallest number that can be written as the sum of two abundant numbers is 24. 
##   By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. 
##   However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that 
##   cannot be expressed as the sum of two abundant numbers is less than this limit.
##
##   Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
##
##   For checking, 1 is the smallest deficient number
##                 6 is the smallest perfect number
##                12 is the smallest abundant number
## The answer is : 4179871
##                 
## Post op: the first method took way over 38 min - the second method took 28 secs - There is a faster way 
## ofcourse, but this would be good enough for me to understand the python programming way

import time


MAXVAL = 28123
divisors = []
perfectNum = []
deficientNum = []
abundantNum = []
list_of_abundantNum_sum = []

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
  base.append(1) ## all number divisible by 1
  for count in range(1,(num+2)/2):
    if ((num % count == 0)):
      base.append(count)
  ## Check for divisible term and shit
  check_for_divisors(base,base,num)


start_time = time.time()

for count in range(1,MAXVAL + 1):
  divisors[:] = []
  sum_of_divisors = 0
  
  check_for_term(count)
  for item in divisors:
    sum_of_divisors += item
  if (sum_of_divisors == count) and (count != 1):
    pass
    ## perfectNum.append(count)
  elif (sum_of_divisors < count) or (count == 1):
    ## deficientNum.append(count)
    pass
  else:
    abundantNum.append(count)

print "Gathering all perfect numbers, Deficient numbers, and abundant numbers from 1 to 28123 takes : ",
print("--- %s seconds ---" % (time.time() - start_time))

'''


### Below code took almost 39 min to complete - too long - I left them here for
### future studying

muNtnadnuba = list(abundantNum)

for item1 in abundantNum:
  for item2 in reversed(muNtnadnuba):
    ## print item1, item2
    new_num = item2 + item1
    if (new_num > MAXVAL):
      continue
    else:
      if (new_num in list_of_abundantNum_sum):
        continue
      else:
        list_of_abundantNum_sum.append(new_num)
    
list_of_abundantNum_sum.sort()
result = 0

for count in range (1, MAXVAL + 1):
  if count in list_of_abundantNum_sum:
    continue
  else:
    result += count
    print count,

print


print result
## print list_of_abundantNum_sum

'''

abundantNum.sort()
look_set_abundantNumbers = set()
for item1 in abundantNum:
  for item2 in abundantNum:
    new_num = item2 + item1
    if (new_num > MAXVAL):
      continue
    else:
      if (new_num in look_set_abundantNumbers):
        continue
      else:
        look_set_abundantNumbers.add(new_num)

result = 0
for count in range (1, MAXVAL + 1):
  if count in look_set_abundantNumbers:
    continue
  else:
    result += count
    ## print count,

print
print result

print("--- %s seconds ---" % (time.time() - start_time))

## The about method would run around 26 secs

