import re
T = int(raw_input())
for i in xrange(T):
    N = raw_input()
    if re.search(r'[A-Z].*[A-Z]', N) and re.search(r'[0-9].*[0-9].*[0-9]', N) and re.search(r'^[a-zA-Z0-9]{10}$', N) and not re.search(r'(.).*\1', N):
        print "Valid"
    else:
        print "Invalid"