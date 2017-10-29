from itertools import product
K, M = map(int, raw_input().split())

L = list()

for _ in xrange(K):
    l = list(map(int, raw_input().split()))
    l.pop(0)
    L.append(l)

S_max = 0

for i in list(product(*L)):
    S = 0
    for j in i:
        S += (j**2)
    S = S % M #has to be on this line and not combined with above
    if S > S_max:
        S_max = S

print S_max