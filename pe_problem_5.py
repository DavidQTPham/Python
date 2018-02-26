#! /usr/bin/python

## 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
## What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
##  (The value I found was: 232,792,560) - was testing from 1 to 1,000,000,000
testvalue = 0



def divisible_in_range(value1,range1, range2):
  # Have to compensate that the python range does not include the final value
  range2 +=1
  for i in range(range1,range2):
    if ((value1 % i) == 0):
      pass
    else:
      return -1
      break
  return value1


def test():
  testvalue1 = int(raw_input("Please input the test value to be divide : "))
  testvalue2 = int(raw_input("Please input the lower range value : "))
  testvalue3 = int(raw_input("Please input the upper range value : "))

  found_one = divisible_in_range(testvalue1, testvalue2, testvalue3)
  if (found_one > 0):
    print ("The smallest number that can be divided by each of the number from " + str(testvalue2) + " to " + str(testvalue3) + " is : " + str(testvalue1))
  else:
    print (str(testvalue1) + " cannot be divided by all number from " + str(testvalue2) + " to " + str(testvalue3))


def test2():

  valueA = int(raw_input("Please input the lower range value to search for the number : "))
  valueB = int(raw_input("Please input the upper range value to search for the number : "))
  valueC = 1
  valueD = 20
  valueA += 1
  counter = 0

  for counter in range (valueA, valueB):
    ## print ("Testing " + str(counter) + " in range " + str(valueA) + " to " + str(valueB)) 
    found_one = divisible_in_range(counter, valueC, valueD)
    if (found_one > 0):
      ## if ((found_one % 2)== 0):
      print ( "found this : " + str(found_one))
    else:
      pass

    
test2()

### Post programming
# found this one on the thread for this problem.  I love it
#  This does not require programming at all. 
# Compute the prime factorization of each number from 1 to 20, and multiply the greatest power of each prime together: 
# 20 = 2^2 * 5 
# 19 = 19 
# 18 = 2 * 3^2 
# 17 = 17 
# 16 = 2^4 
# 15 = 3 * 5 
# 14 = 2 * 7 
# 13 = 13 
# 11 = 11 
# All others are included in the previous numbers. 
# ANSWER: 2^4 * 3^2 * 5 * 7 * 11 * 13 * 17 * 19 = 232 792 560  
