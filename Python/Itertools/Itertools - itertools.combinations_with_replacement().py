from itertools import combinations_with_replacement

S, k = raw_input().split()
S = list(S)


for i in list(combinations_with_replacement(sorted(S), int(k))):
    ans = ""
    for j in i:
        ans += j
    print ans