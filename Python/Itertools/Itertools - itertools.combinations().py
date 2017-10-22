from itertools import combinations

S, k = raw_input().split()
S = list(S)

for x in xrange(1,int(k)+1):
    for i in list(combinations(sorted(S), x)):
        ans = ""
        for j in i:
            ans += j
        print ans