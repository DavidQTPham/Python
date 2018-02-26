#! /usr/bin/python
# -*- coding: utf-8 -*-
#
#  Counting Sundays
#  Problem 19
#
#   You are given the following information, but you may prefer to do some research for yourself.
#
#    1 Jan 1900 was a Monday.
#    Thirty days has September,
#    April, June and November.
#    All the rest have thirty-one,
#    Saving February alone,
#    Which has twenty-eight, rain or shine.
#    And on leap years, twenty-nine.
#    A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
#
#   How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

monthsDict = {"January":31, "February":28, "March":31, "April":30, "May":31, "June":30,\
              "July":31, "August":31, "September":30, "October":31, "November":30, "December":31}

weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
months = ["January","February","March","April", "May", "June","July","August","September",\
          "October", "November", "December"]


days_per_year = 365
moddays = 0
total_days = 0

def is_leap(year):
  if ((year % 4) == 0):
    if ((year % 100 == 0) and (year % 400 == 0)):
      return True
    elif (year % 100 == 0):
      return False
    else: 
      return True
  else:
    return False


def find_weekday(year, month, day):
  ## known week_day
  ## Jan 01, 1900 is a Monday
  ## So Jan 08, 1900 is a Sunday
  global total_days
  total_days = 0
  extra_day = 0
  mod_result = 0
  ind = 0
  index = 0
  sunday_index = 0
  offset_day = 0
  start_sunday = 0

  for count in range(1900, year):
    if (is_leap(count)):
      total_days += (days_per_year + 1)
    else:
      total_days += days_per_year
  
  ## Since we only count up to the year before the year that we wanted to know
  ## we have to adjust a bit
  if (is_leap(count + 1)):
    ## print (str(count + 1) + " is a leap year")
    if (month > 1):
      extra_day += 1
    else:
      extra_day = 0

  if ((month == 1) and (day == 1)):
     pass
  else:
    for count in range(0,month -1):
      ind = months[count]
      total_days += monthsDict[ind]
  total_days += (extra_day + day) - 8
  mod_result = (total_days % 7)
  
  index = weekdays[mod_result]
  sunday_index = weekdays.index("Sunday")
  offset_day = sunday_index - weekdays.index(index)
  start_sunday = 1 + offset_day

  return index

## for month in months:
##  print month,monthsDict[month]
print "---------------------------------------"
outp = find_weekday(2000,01,01)
print ("01 01 2000  fell on " + outp)
outp = find_weekday(2000,12,31)
print ("12 31 2000  fell on " + outp)
outp = find_weekday(2009,12,31)
print ("12 31 2009  fell on " + outp)
outp = find_weekday(1964,07,04)
print ("07 04 1964  fell on " + outp)
outp = find_weekday(1997,11,15)
print ("11 15 1997  fell on " + outp)
outp = find_weekday(1996,8,1)
print ("08 01 1996  fell on " + outp)
print "-------------------------"

total_sundays_on_the_first = 0
linenumber = 1
for count1 in range(1901, 2001):
  outp = ""
  for count2 in range(1, 13):
    outp = find_weekday(count1, count2, 1)
    ## print (outp + ", " + str(count2) + " 1, " + str(count1))
    if (outp == "Sunday"):
      print "Found a sunday ",
      total_sundays_on_the_first += 1
      print total_sundays_on_the_first
      print (linenumber,outp, count2, "1", count1)
      linenumber += 1
    outp = ""
print ("There were " + str(total_sundays_on_the_first) + " sundays that fell on the 1st day of the month from the year of \
1901 to the year of 2000.")

## Post op - Mine said it is 172, answer said 171 - Where did my extra sunday come from? 
