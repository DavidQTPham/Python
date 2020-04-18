#! /usr/bin/python

# This is the first problem of the Project Euler.net
# Problem 1
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get:3, 5, 6, 9.  
# If we add 3,5,6,9, we would get 23
# Challenge:
# The sum of all multiples of 3 or 5 below 1000

finalValue = 0
# if included the value 1000, result would not be correct since they asked for below 1000
# but hey I am a rebel
for counter in range(1, 1001):
  # print(counter)
  if (counter % 3 == 0):
    print("Divisible by 3: " + str(counter))
    finalValue+=counter
  elif (counter % 5 == 0):
    print("Divisible by 5: " + str(counter))
    finalValue+=counter

print (finalValue)

