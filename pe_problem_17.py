#! /usr/bin/python
# -*- coding: utf-8 -*-

## Number letter counts
# Problem 17
# 
# If the numbers 1 to 5 are written out in words: one, two, three, four, five, 
# then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
#
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, 
# how many letters would be used?
# 
# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 
# letters and 115 (one hundred and fifteen) contains 20 letters. 
# The use of "and" when writing out numbers is in compliance with British usage.

total_comp_words = ""
total_words = ""

def check_1(mword):
  if (mword == "1"):
    return "one"
  elif (mword == "2"):
    return "two"
  elif (mword == "3"):
    return "three"
  elif (mword == "4"):
    return "four"
  elif (mword == "5"):
    return "five"
  elif (mword == "6"):
    return "six"
  elif (mword == "7"):
    return "seven"
  elif (mword == "8"):
    return "eight"
  elif (mword == "9"):
    return "nine"
  else:
    return "zero"

def check_2(w1, w2):

  tmpw = ""
  if (w1 == "one"):
    tmpw += "ten"
  elif (w1 == "two"):
    tmpw += "twenty"
  elif (w1 == "three"):
    tmpw += "thirty"
  elif (w1 == "four"):
    tmpw += "forty"
  elif (w1 == "five"):
    tmpw += "fifty"
  elif (w1 == "six"):
    tmpw += "sixty"
  elif (w1 == "seven"):
    tmpw +=  "seventy"
  elif (w1 == "eight"):
    tmpw += "eighty"
  elif (w1 == "nine"):
   tmpw += "ninety"
  if (w2 == "zero"):
    return tmpw
  elif (w1 == "one"):
    if (w2 == "one"):
      return "eleven"
    elif (w2 == "two"):
      return "twelve"
    elif (w2 == "three"):
      return "thirteen"
    elif (w2 == "four"):
      return "fourteen"
    elif (w2 == "five"):
      return "fifteen"
    elif (w2 == "six"):
      return "sixteen"
    elif (w2 == "seven"):
      return "seventeen"
    elif (w2 == "eight"):
      return "eighteen"
    else:
      return "nineteen"
  else:
    tmpw += " " + w2
    return tmpw

def check_3(w1, w2, w3):


  tmpw1 = ""
  tmpw2 = ""
  if (w1 == "one"):
    tmpw1 += "one hundred"
  elif (w1 == "two"):
    tmpw1 += "two hundred"
  elif (w1 == "three"):
    tmpw1 += "three hundred"
  elif (w1 == "four"):
    tmpw1 += "four hundred"
  elif (w1 == "five"):
    tmpw1 += "five hundred"
  elif (w1 == "six"):
    tmpw1 += "six hundred"
  elif (w1 == "seven"):
    tmpw1 += "seven hundred"
  elif (w1 == "eight"):
    tmpw1 += "eight hundred"
  else:
    tmpw1 += "nine hundred" 
  if ((w2 == "zero") and (w3 == "zero")):
    return tmpw1
  else:
    tmpw2 = check_2(w2,w3)
    return (tmpw1 + " and " + tmpw2)

def check_4(w1, w2, w3, w4):

  tmpw1 = ""
  tmpw2 = ""
  
  if (w1 == "one"):
    tmpw1 += "one thousand"
  elif (w1 == "two"):
    tmpw1 += "two thousand"
  elif (w1 == "three"):
    tmpw1 += "three thousand"
  elif (w1 == "four"):
    tmpw1 += "four thousand"
  elif (w1 == "five"):
    tmpw1 += "five thousand"
  elif (w1 == "six"):
    tmpw1 += "six thousand"
  elif (w1 == "seven"):
    tmpw1 += "seven thousand"
  elif (w1 == "eight"):
    tmpw1 += "eight thousand"
  else:
    tmpw1 += "nine thousand"
  if ((w2 == "zero") and (w3 == "zero") and (w4 == "zero")):
    return tmpw1
  else:
    tmpw2 = check_3(w2,w3,w4)  
    return (tmpw1 + " " + tmpw2)


def translate_num_to_word(num):
  
  result = 0
  mword = str(num)
  max_count = len(mword)
  if (max_count == 1):
    result = check_1(mword)
    return result
  elif (max_count == 2):
    tmp_word1 = check_1(mword[0])
    tmp_word2 = check_1(mword[1])
    result = check_2(tmp_word1, tmp_word2)
    return result
  elif (max_count == 3):
    temp_word1 = check_1(mword[0])
    temp_word2 = check_1(mword[1])
    temp_word3 = check_1(mword[2])
    result = check_3(temp_word1, temp_word2, temp_word3)
    return result
  elif (max_count == 4):
    temp_word1 = check_1(mword[0])
    temp_word2 = check_1(mword[1])
    temp_word3 = check_1(mword[2])
    temp_word4 = check_1(mword[3])
    result = check_4(temp_word1, temp_word2, temp_word3, temp_word4)
    return result
  else:
    return "under construction"

for counter in range(1, 1001):
  myword = translate_num_to_word(counter)
  total_comp_words += myword
  myword = myword + ", "
  total_words += myword
  

print total_words

total_letters = 0
for count in range(0,len(total_comp_words)):
  if (total_comp_words[count] != " "):
    total_letters += 1

print ("The total letters used is " + str(total_letters))
