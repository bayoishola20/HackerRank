import re
S = raw_input()
k = raw_input()
pattern = re.finditer(r'(?=('+k+'))', S)

if re.search(r'(?=('+k+'))', S):
    for i in pattern:
        print (i.start(1), i.end(1) - 1)
else:
    print (-1, -1)