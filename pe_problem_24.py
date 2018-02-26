#! /usr/bin/python
# -*- coding: utf-8 -*-
#
## Lexicographic permutations
## Problem 24
##
## A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. 
## If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. 
## The lexicographic permutations of 0, 1 and 2 are:
##
##       012   021   102   120   201   210
##
## What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

import itertools
count = 0
mylist = [0,1,2,3,4,5,6,7,8,9]


def permutations(iterable, r=None):
  global count
  # permutations('ABCD', 2) --> AB AC AD BA BC BD CA CB CD DA DB DC
  # permutations(range(3)) --> 012 021 102 120 201 210
  pool = tuple(iterable)
  n = len(pool)
  r = n if r is None else r
  if r > n:
    return
  indices = range(n)
  cycles = range(n, n-r, -1)
  yield tuple(pool[i] for i in indices[:r])
  while n:
    for i in reversed(range(r)):
      cycles[i] -= 1
      if cycles[i] == 0:
        indices[i:] = indices[i+1:] + indices[i:i+1]
        cycles[i] = n - i
      else:
        j = cycles[i]
        indices[i], indices[-j] = indices[-j], indices[i]
        yield tuple(pool[i] for i in indices[:r])
        break
        return
    else:
      return

counter = 0
answer = permutations(mylist,10)
for result in answer:
  ## print counter, result
  counter += 1
  if (counter == 1000000):
    print counter, result
    break

