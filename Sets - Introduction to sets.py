#==================== GIVEN CODE ======================#
from __future__ import division
#===================== END =========================#


def average(array):
    # your code goes here
    i = set(array)
    result = sum(i) / len(i)
    return result


#==================== GIVEN CODE ======================#
if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    result = average(arr)
    print result
#===================== END =========================#