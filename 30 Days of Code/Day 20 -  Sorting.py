#!/bin/python

import sys

n = int(raw_input().strip())
a = map(int, raw_input().strip().split(' '))
# Write Your Code Here
numSwaps = 0
for i in xrange(n):
    for j in xrange(n-1):
        if a[j] > a[j+1]:
            temp = a[j]#where temp is a temporary variable as we swap elements
            a[j] = a[j+1]
            a[j+1] = temp
            numSwaps += 1

    if (numSwaps == 0):
        break

print "Array is sorted in " + str(numSwaps) + " swaps."
print "First Element: " + str(a[0])
print "Last Element: " + str(a[-1])