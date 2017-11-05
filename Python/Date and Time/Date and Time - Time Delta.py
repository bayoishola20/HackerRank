#!/bin/python3

import sys
from datetime import datetime

def time_delta(t1, t2):
    # Complete this function
    d_t1 = datetime.strptime(t1, "%a %d %b %Y %H:%M:%S %z")
    d_t2 = datetime.strptime(t2, "%a %d %b %Y %H:%M:%S %z")
    return (abs(int((d_t1-d_t2).total_seconds())))


if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        t1 = input().strip()
        t2 = input().strip()
        delta = time_delta(t1, t2)
        print(delta)