import re
T = int(raw_input().strip())
for i in xrange(T):
    try:
        re.compile(raw_input())
        print "True"
    except re.error:
        print "False"