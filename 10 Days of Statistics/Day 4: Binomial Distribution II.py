ratio = list(map(float, raw_input().split()))
p = (ratio[0]/100) #probability (success) of rejected
n = 10

def factorial(n):
    if n > 1:
        return factorial(n - 1) * n
    if n == 1 or n == 0:
        return 1


def binomial(r, n, p):
    c = factorial(n) / (factorial(n - r) * factorial(r)) # binomial coefficient or combination: n!/r!*(n-r)!
    return c * p**r * (1.0 - p)**(n-r)

#At most two rejects
ans1 = 0
for i in range(n):
    if i < 3:
        ans1 += binomial(i, n, p)
        
print round(ans1, 3)

#At least two rejects
ans2 = 0
for i in range(n):
    if i > 1:
        ans2 += binomial(i, n, p)

print round(ans2, 3)