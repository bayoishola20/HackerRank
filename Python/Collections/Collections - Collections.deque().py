from collections import deque
n = int(raw_input())
d = deque()

for i in xrange(n):
    data = raw_input().split()
    if len(data) == 1:
        if data[0] == "pop":
            d.pop()
        if data[0] == "popleft":
            d.popleft()
    if len(data) > 1:
        if data[0] == "append":
            d.append(int(data[1]))
        if data[0] == "appendleft":
            d.appendleft(int(data[1]))
for j in d:
    print j,