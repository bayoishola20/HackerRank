#!/bin/python

import sys
check = 0
answer = 0
n = int(raw_input().strip())
while n >= 1:
    if n % 2 == 1:
        answer += 1
        if answer > check:
            check = answer
    else:
        answer = 0
    n //= 2 #ensures that we are only picking consecutive 1s
print check