#! /usr/bin/python
# -*- coding: utf-8 -*-

m = 1
n = 1
a = 0
b = 0
c = 0
sumval = 0

while (sumval < 1500 ):
  m+=1
  for n in range (1, m):
    b = 2*m*n
    a = (m * m) - (n * n)
    c = (m * m) + (n * n)
    if ((c * c) == ((a * a) + (b * b))):
      sumval = a + b + c
      myproduct = a * b * c
      print ("a = " + str(a) + "; b = " + str(b) + "; c = " + str(c) + "; m = " + str(m) + " ; n = " + str(n) + "; sum = " + str(sumval) + "; Product = " + str(myproduct))
      if (sumval == 1000):
        print ("found it!")

