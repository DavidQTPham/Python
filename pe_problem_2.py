#! /usr/bin/python

# Even Fibonacci numbers
# Each new term in the Fibonacci sequence is generated by adding the previous two terms.  By starting
# with 1 and 2, the first 10 terms will be
#    1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
#
# By considering the terms in Fibonacci sequence whose values do not exceed four million, 
# find the sum of the even-value terms

MAX = 4000000
term1 = 1
term2 = 0
newterm = 0
finalValue = 0

while (newterm < 4000000):
  newterm = term1 + term2
  print (newterm)
  term1 = term2
  term2 = newterm
  if ((newterm < 4000000) and (newterm % 2 == 0)):
    print ("even Fibonacci number: " + str(newterm))
    finalValue += newterm

print ("The sum of the even Fibonacci's values is: " + str(finalValue))