#! /usr/bin/python
# -*- coding: utf-8 -*-

## The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
##
## Find the sum of all the primes below two million.
import math

sumOFprime = 0

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


for p in range(2, 2000000):
  if is_prime(p):
    sumOFprime += p
    print(str(p))
print ("Sum of prime from 2 to 2,000,000 is :" + str(sumOFprime))

