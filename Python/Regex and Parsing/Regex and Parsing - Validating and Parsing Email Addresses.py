import re, email.utils
n = int(raw_input())

for i in xrange(n):
    addr = raw_input()
    pair = email.utils.parseaddr(addr)
    if re.match(r"^[a-zA-Z]{1}\w+_*-*.*@[a-zA-Z]+\.[a-zA-Z]{1,3}$", pair[1]):
        print addr