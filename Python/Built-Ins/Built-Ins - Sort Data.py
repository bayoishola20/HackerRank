import sys

if __name__ == "__main__":
    n, m = raw_input().strip().split(' ')
    n, m = [int(n), int(m)]
    arr = []
    for arr_i in xrange(n):
        arr_temp = map(int,raw_input().strip().split(' '))
        arr.append(arr_temp)
    k = int(raw_input().strip())
    
    table = sorted(arr, key=lambda x:x[k])
    
    for i in xrange(n):
        line = ""
        for j in xrange(m):
            line += str(table[i][j]) + ' '
        print line