from itertools import permutations

S, k = raw_input().split()
S = list(S)


for i in list(permutations(sorted(S), int(k))):
    ans = ""
    for j in i:
        ans += j
    print ans