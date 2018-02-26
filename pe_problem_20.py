#! /usr/bin/python
# -*- coding: utf-8 -*-
#
#  Factorial digit sum
#  Problem 20
#
#  n! means n × (n − 1) × ... × 3 × 2 × 1
#
#  For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
#  and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
#
#  Find the sum of the digits in the number 100!


def factor(n):

  if (n==1):
    return 1
  else:
    return n*factor(n-1)


result = factor(100)
print result
result_in_char = str(result)
print result_in_char
sum_of_val = 0
for letter in result_in_char:
  sum_of_val += int(letter)

print sum_of_val
