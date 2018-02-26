#! /usr/bin/python

#
#  Largest Prime Factor
# The prime factors of 12195 are 5, 7, 13 and 29
# what is the largest prime factor of the number 600851475143 ?
#
# solution 1:
# a) Find the prime number from 1 to 600851475143
#    background: A prime number is a whole number greater than 1, whose only two whole number factors are
#                1 and itself.  The first few prime numbers are 2,3,5,7,11,13,17,19,23, 29, ...
# 
# Currently there is no efficient algorithm for this method, really, imho.
# 
import math
Target = 600851475143
dividend = 0 
result = 0
primelist = []

def is_prime(n):
  for i in range(2, n):
    if n%i == 0:
      return False
  return True

def factorThis(value, number):
  global result
  tempval = 0
  if (number > value):
    return 0
  elif (number == value):
    result = result + 1
    return result 
  else:
    if ((value % number) == 0):
      tempval = int((float(value) / number) + 0.5)
      tempfac = factorThis(tempval, number)
      result = result + 1
    else:
      return 0
  return result


def userinput():
  global dividend
  dividend = int(raw_input("Please enter the number you want to factor: "))
  if (dividend > 10000):
    newnum = int(math.sqrt(dividend) * 2.2)
  else:
    newnum = dividend
  ## generate prime list
  print ("generate prime list")
  for p in range(2, newnum +1):
    if is_prime(p):
      primelist.append(p)  
  print primelist
  if dividend in primelist:
    print ("Largest prime factor for " + str(dividend) + " is : " + str(dividend))
  return


def findAllfactor(value1):
  largestPrime = 0
  largestNum = math.sqrt(value1) * 2
  leftover = 0
  global result
  print("2 times The largest number obtained from taking squareroot of " + str(value1) + " is " + str(largestNum))
  for i in primelist:
    if (i > largestNum):
      largestPrime = i
      break
  print("Largest Prime found : " + str(largestPrime))
  
  for i in primelist:
    if (i == largestPrime):
      break
    else:
      result = 0
      factorv = factorThis(value1, i)
      if (factorv != 0):
        if (math.pow(i,factorv) == value1):
          leftover = 0
          break
        else:
          leftover = int(value1 /(math.pow(i,factorv)))
          if leftover in primelist:
            print ("factorv : " + str(factorv) + "; i : " + str (i))
            print ("The largest prime factor for value " + str(dividend) + " is : " + str(leftover))
            ## break
          else:
            value1 = leftover
        print ("factorv : " + str(factorv) + "; i : " + str (i) + "; Leftover : " + str(leftover))
      else:
        ## print ("There is no factor for " + str(value1) + " divided by : " + str(i))
        pass
  return





userinput()
findAllfactor(dividend)
