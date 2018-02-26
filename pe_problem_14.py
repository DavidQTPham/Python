#! /usr/bin/python
# -*- coding: utf-8 -*-
##
## The following iterative sequence is defined for the set of positive integers:
##
##  n → n/2 (n is even)
##  n → 3n + 1 (n is odd)
##
##  Using the rule above and starting with 13, we generate the following sequence:
##  13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
##
##  It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), 
##  it is thought that all starting numbers finish at 1.
##
##  Which starting number, under one million, produces the longest chain?
## 
##  NOTE: Once the chain starts the terms are allowed to go above one million.


counter = 0
longest_term = 0
# record = []

def my_sequence(startingPoint):

  global counter
  ## global record
  if ((startingPoint % 2) == 0):
    counter += 1
    # record.append(startingPoint/2)
    my_sequence(startingPoint/2)
  elif ( startingPoint > 1):
    counter += 1
    # record.append(startingPoint * 3 + 1)
    my_sequence(startingPoint * 3 + 1)
  else:
    ## record.append(1)
    counter += 1
  return


## startingnumber = 13
## my_sequence(startingnumber)
## print ("For starting number = " + str(startingnumber) + ", the number of term is " + str(counter))


for i in range(1, 1000000):
  counter = 0
  ## record[:] = []
  ## record.append(i)
  my_sequence(i)
  if (longest_term < counter):
    longest_term = counter
    print ("New longest term found : " + str(longest_term) + " at starting number " + str(i))
    
  ## print record
