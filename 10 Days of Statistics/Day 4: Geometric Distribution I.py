prob = list(map(float, raw_input().split()))
p = prob[0] / prob[1] #success
q = 1 - p #failure
n = 5

#geometric distribution formular
ans = q ** (n - 1) * p
print round(ans, 3)