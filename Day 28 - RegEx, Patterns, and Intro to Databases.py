#!/bin/python

import sys
import re

arr = [] #this must be of a global scope

N = int(raw_input().strip())
for a0 in xrange(N):
    firstName,emailID = raw_input().strip().split(' ')
    firstName,emailID = [str(firstName),str(emailID)]
    
    
    if re.search("^[\w.+\-]+@gmail\.com$", emailID):
        arr.append(firstName)

arr.sort()

for firstName in arr:
    print firstName