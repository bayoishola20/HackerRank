#!/bin/python

import sys


arr = []
for arr_i in xrange(6):
   arr_temp = map(int,raw_input().strip().split(' '))
   arr.append(arr_temp)
    
max_possibility = -9 * 7

for i in xrange(0,5):
    for j in xrange(0,5):
        if i + 1 < 5 and j + 1 < 5:
            result = arr[i][j] + arr[i][j + 1] + arr[i][j + 2] + arr[i + 2][j] + arr[i + 2][j + 1] + arr[i + 2][j + 2] + arr[i + 1][j + 1] #derived from the shape of an hour glass 3--1--3
            if result > max_possibility:
                max_possibility = result     
print max_possibility