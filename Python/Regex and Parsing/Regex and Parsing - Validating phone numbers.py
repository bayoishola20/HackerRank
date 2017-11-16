import re
N = raw_input()

for i in xrange(int(N)):
    if re.match(r"^[7-9]{1}[0-9]{9}$", raw_input()):
        print "YES"
    else:
        print "NO"