from itertools import groupby
groups = []
S = raw_input()

for key, value in groupby(S):
    groups.append(list(key)) 
    print (len(list(value)), int(key)),