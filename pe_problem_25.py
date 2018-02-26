#! /usr/bin/python
# -*- coding: utf-8 -*-

##1000-digit Fibonacci number
## Problem 25
##
##  The Fibonacci sequence is defined by the recurrence relation:
##
##    Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
## 
## Hence the first 12 terms will be:
##
##    F1 = 1
##    F2 = 1
##    F3 = 2
##    F4 = 3
##    F5 = 5
##    F6 = 8
##    F7 = 13
##    F8 = 21
##    F9 = 34
##    F10 = 55
##    F11 = 89
##    F12 = 144
##
## The 12th term, F12, is the first term to contain three digits.
##
## What is the index of the first term in the Fibonacci sequence to contain 1000 digits?

not_found = 1
term1 = 1
term2 = 1
index = 2

def fibonacci(v1, v2):

  return v1 + v2

def count_sequence_digit(value):
  return len(str(value))

while (not_found):
  
  if (index > 2):
    index += 1
    new_term = fibonacci(term1, term2)
    howlong = count_sequence_digit(new_term)
    if (howlong == 1000):
      ## print "Found it ", index
      not_found = 0
    else:
      ## print index, term1, term2, new_term
      term1 = term2
      term2 = new_term
  else:
    new_term = fibonacci(term1, term2)
    index += 1
    term1 = term2
    term2 = new_term
  
print ("The index of the Fibonacci sequence that contains 1000 digits is " + str(index))
