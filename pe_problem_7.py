#! /usr/bin/python
## By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
## What is the 10 001st prime number?

counter = 0
p = 0
counter = 0
lastprime = 2

def is_prime(n):
  for i in range(2, n):
    if n%i == 0:
      return False
  return True




newnum = int(raw_input("Please input the upper range that you think included the 10001 prime number : "))

for p in range(2, newnum +1):
  if is_prime(p):
    counter += 1
    if (counter == 10001):
      print ("The 10001th prime number is : " + str(p))
      break

## answer is: 104743
## Post op: This code produced the slowest prime lookup number ever - Don't use this one
