#! /usr/bin/python
# -*- coding: utf-8 -*-

## Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, 
## there are exactly 6 routes to the bottom right corner.
## How many such routes are there through a 20×20 grid?

## let's use numpy
import numpy

#3 Notice, eventhough it is a 20 x 20 grid, but this is a non-zero starting, so grid scale becomes 21 x 21

max_X = 21
max_Y = 21
total_paths = 0

## Create an array of max_X rows and max_Y columns and fill them with zeroz
grid = numpy.zeros((max_Y+1,max_X+1),dtype=numpy.int64)

## There are few ways to deal with this problem - It's known as the lattice traversing
## One can crank and solve it using the formular which is (M+N)!/(M! * N!)
## or writing out the Pascal triangle
##
##      1   1   1   1    1    1
##      1   2   3   4    5    6
##      1   3   6   10   15   21
##      1   4  10   20   35   56
##      1   5  15   35   70   126
##      1   6  21   56   126  252
##
## So you can calculate the path using this way as well
##
## One of my colleague used brute force to calculate the possible routes
## and sabre has another way to solve it
##
## For now I am going to use the Pascal Triangle

## First, the boundaries have only one path per direction

def print_grid():

  for i in range(0,max_X):
    for j in range (0, max_Y):
      print '{:11d}'.format(grid[i,j]),
    print
    print

for column in range (0,max_Y+1):
  grid[0][column] = 1
for row in range (0,max_X+1):
  grid[row][0] = 1

## print_grid()
print
print

for column in range (1,max_Y):
  for row in range (1,max_X):
    grid[row][column] = grid[row-1][column] + grid[row][column -1]

print_grid()
