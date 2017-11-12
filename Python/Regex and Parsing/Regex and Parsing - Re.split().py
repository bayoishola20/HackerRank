import re
S = raw_input()
for i in re.split(r'[,\.]', S):
    if len(i) > 0:
        print i