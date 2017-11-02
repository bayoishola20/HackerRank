from collections import defaultdict
n, m = list(map(int, raw_input().split()))
d = defaultdict(list)

for i in xrange(n):
    d[raw_input()].append(i+1)
for j in xrange(m):
    x = raw_input()
    if x in d:
        print ' '.join(map(str, d[x]))
    else:
        print "-1"