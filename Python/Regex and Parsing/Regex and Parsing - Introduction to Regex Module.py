import re
T = int(raw_input())
for i in xrange(T):
    s = raw_input()
    pattern = re.match(r'^[+-]?\d*\.\d+$',s)
    if pattern:
        print True
    else:
        print False