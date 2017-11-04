from collections import deque
T = int(raw_input()) #number of test cases

for i in xrange(T):
    n = int(raw_input())
    data = deque(list(map(int, raw_input().split())))
    current = 0
    if data[-1] < data[0]:
        current = data.popleft()
    else:
        current = data.pop()
    while len(data) > 0:
        if data[-1] <= data[0] and current >= data[0]:
            current = data.popleft()
        elif data[-1] >= data[0] and current >= data[1]:
            current = data.pop()
        else:
            break
    if len(data) == 0:
        print "Yes"
    else:
        print "No"