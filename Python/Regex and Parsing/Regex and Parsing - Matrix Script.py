#!/bin/python

import sys,re,itertools


n, m = raw_input().strip().split(' ')
n, m = [int(n), int(m)]
matrix = []
matrix_i = 0
for matrix_i in xrange(n):
    matrix_t = raw_input()
    matrix.append(matrix_t)
    result = str()
for i in list(itertools.izip(*matrix)):
    result += ('').join(i)


print (re.sub(r'(?<=([0-9A-Za-z]))\W+(?=([0-9A-Za-z]))', " ", result))