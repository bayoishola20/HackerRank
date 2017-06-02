#!/bin/python

import sys


N = int(raw_input().strip())



if N % 2 == 0 and (2 <= N <= 5 or N > 20):
        print "Not Weird"
else:
    print "Weird"