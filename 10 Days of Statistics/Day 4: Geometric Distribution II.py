prob = list(map(float, raw_input().split()))
p = prob[0] / prob[1] #success
q = 1 - p #failure
n = 5

#geometric distribution formular
ans = 0

for i in xrange(n + 1):
    if i > 0:
        ans += q ** (i - 1) * p
print round(ans, 3)