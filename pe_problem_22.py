#! /usr/bin/python
# -*- coding: utf-8 -*-
##  Names scores
##  Problem 22
## 
##  Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, 
##  begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value
##  by its alphabetical position in the list to obtain a name score.
##
## For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, 
## is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.
##
## What is the total of all the name scores in the file?

FILE_NAME = "names.txt"
PATH = "./"

ALPHA_DICT = {'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,'J':10,'K':11,'L':12,'M':13,'N':14,\
              'O':15,'P':16,'Q':17,'R':18,'S':19,'T':20,'U':21,'V':22,'W':23,'X':24,'Y':25,'Z':26}

def get_file_and_sort():
  ## This is the best way to handle a file open and closing
  with open(PATH + FILE_NAME) as myfile:
    ## file contains names with comma delimiters - Use this function to read all and split them out and 
    ## store into a list
    mystring = ""
    ## Have to replace newline with a nothing char, otherwise dictionary lookup routine would fail
    mystring = myfile.read().replace('\n','')
    namesList = mystring.split(',')
  ## sort it out alphabetically
  namesList.sort()
  return namesList



mylist = get_file_and_sort()
counter = 1
name_score = 0
score = 0
total_score = 0
for name in mylist:
  for ch in name:
    name_score += ALPHA_DICT[ch]
    print ch,ALPHA_DICT[ch],
  print
  score = name_score * counter
  print counter, name, name_score, score
  name_score = 0
  counter += 1
  total_score += score
  score = 0
print "Total name score for this file is: ", total_score
