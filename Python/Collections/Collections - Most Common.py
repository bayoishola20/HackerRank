#!/bin/python
from collections import Counter
import sys

if __name__ == "__main__":
    s = raw_input().strip()
    i = Counter(s)
    most_common = i.most_common()
    j = sorted(most_common, key=lambda x: (-x[1], x[0])) # minus(-) for reverse
    
    for k in xrange(3):
        print j[k][0], j[k][1]