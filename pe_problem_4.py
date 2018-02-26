#! /usr/bin/python

##  A palindromic number reads the same both ways. 
##  The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.
##  Find the largest palindrome made from the product of two 3-digit numbers
counter1 = 0
counter2 = 0
result = 0
topvalue = 0

def is_palindrome(value1):
  ## Check for palindrome
  placeholder = str(value1).lower()
  str_length = len(value1)
  midstring = int(str_length /2)
  left_position = 0
  right_position = str_length -1
  while (left_position < midstring):
    if (placeholder[left_position] == placeholder[right_position]):
      left_position +=1
      right_position -=1
    else:
      return False
  return True


for counter1 in range(1, 1000):
  for counter2 in range(1,1000):
    result = counter1 * counter2
    if (is_palindrome(str(result))):
      if (topvalue < result):
        topvalue = result
        value1 = counter1
        value2 = counter2

print ("The largest palindrome made by the product of 3 digits is : " + str(topvalue) + " = " + str(value1) + " x " + str(value2)) 

# checkvalue = raw_input("Check to see if the input meets the palidrome : ")
# if(is_palindrome(checkvalue)):
#  print ("Yes it is")
# else:
#  print ("No it is not")
