#! /usr/bin/python
# -*- coding: utf-8 -*-
#
#
# By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.
#
#                                                  3
#                                                 7 4
#                                                2 4 6
#                                               8 5 9 3
#
# That is, 3 + 7 + 4 + 9 = 23.

#  Find the maximum total from top to bottom of the triangle below:
# 
#                                                  75
#                                                 95 64
#                                               17 47 82
#                                              18 35 87 10
#                                            20 04 82 47 65
#                                          19 01 23 75 03 34
#                                         88 02 77 73 07 63 67
#                                        99 65 04 28 06 16 70 92
#                                       41 41 26 56 83 40 80 70 33
#                                     41 48 72 33 47 32 37 16 94 29
#                                   53 71 44 65 25 43 91 52 97 51 14
#                                 70 11 33 28 77 73 17 78 39 68 17 57
#                               91 71 52 38 17 14 91 43 58 50 27 29 48
#                              63 66 04 68 89 53 67 30 73 16 69 87 40 31
#                            04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
#
# NOTE: As there are only 16384 routes, it is possible to solve this problem by trying every route. However, Problem 67, 
# is the same challenge with a triangle containing one-hundred rows; it cannot be solved by brute force, and requires a clever method! ;o)


max_x = 15
max_y = 32


grid = [[0 for x in range (0, max_x)] for y in range (0, max_y)]

def print_grid():

  print
  for x in range (0, max_x):
    print
    for y in range (0, max_y):
      print '{:3d}'.format(grid[y][x]),
  print

with open('pe_problem_18_data.txt') as f:
  lines_array = []
  for line in f:
    lines_array.append(line.rstrip('\n'))
f.close()

start_column = max_y /2
start_row = 0
left_pos = 0

grid[start_column][start_row] = int(lines_array[0])
for count in range (1, max_x):
  data = lines_array[count].split(" ")
  str_length = len(data)
  left_pos = start_column - str_length + 1
  for i in range (0, str_length):
    grid[left_pos][count] = int(data[i])
    left_pos += 2
  
print_grid()

# find the largest number
# This was my thinking - One starts at a specific location, and from there, one could exam the left value or the right.
# If a desired value is found, the position pointer would be moved to there.  The next value to be examed must be below 
# and locate on either left or right from the current value.  There is no far reach - 
#
# But after I coded up that way, the results were not correct - Even though the next value could be found and chosen, but
# the next next value should also be considered as well, for their sum could be bigger than the one with a bigger value
# for example, from the beginning at value 75, I can see that the next two values are 95 and 64 - If one just choose the value
# 95 over 64 but did not check the next route 95 + 47 is less than 64 + 82 - So to find a proper path, one should at least consider 
# put in the check for one more extra path


total_value = 0
cell_path = []
total_value += grid[start_column][start_row]
## print grid[start_column][start_row]
cell_path.append(start_row)
cell_path.append(start_column)
next_left_left_value = 0
next_left_right_value = 0
next_right_left_value = 0
next_right_right_value = 0
go_left = False
look_ahead_right_value = 0
look_ahead_left_value = 0

for count in range (1, max_x):
  left_value = grid[start_column -1][count]
  right_value = grid[start_column +1][count]
  if (count + 1 < max_x):
    next_left_left_value = grid[start_column -2][count + 1]
    next_left_right_value = grid[start_column][count +1]
    next_right_left_value = grid[start_column][count + 1]
    next_right_right_value = grid[start_column + 2][count +1]
    if (next_left_left_value > next_left_right_value):
      look_ahead_left_value = left_value + next_left_left_value
    else:
      look_ahead_left_value = left_value + next_left_right_value
    if (next_right_left_value > next_right_right_value):
      look_ahead_right_value = right_value + next_right_left_value
    else:
      look_ahead_right_value = right_value + next_right_right_value
    if (look_ahead_left_value > look_ahead_right_value):
      go_left = True
    else:
      go_left = False
  else:
    if (left_value > right_value):
      go_left = True
    else:
      go_left = False
   

  if (go_left):
    start_column = start_column -1
    total_value += grid[start_column][count]
    cell_path.append(count)
    cell_path.append(start_column)
    ## print grid[start_column][count]
  else:
    start_column = start_column + 1
    total_value += grid[start_column][count]
    cell_path.append(count)
    cell_path.append(start_column)
    ## print grid[start_column][count]
 

print ("The highest value found is " + str(total_value)) 


