n = 6
ratio = list(map(float, raw_input().split()))
p = ratio[0]/(ratio[0]+ratio[1]) #probability (success) it is a boy; failure would be: q = 1 -p

def factorial(n):
    if n > 1:
        return factorial(n - 1) * n
    if n == 1 or n == 0:
        return 1


def binomial(r, n, p):
    c = factorial(n) / (factorial(n - r) * factorial(r)) # binomial coefficient or combination: n!/r!*(n-r)!
    return c * p**r * (1.0 - p)**(n-r)

#at least 3 boys
ans = binomial(3,n,p) + binomial(4,n,p) + binomial(5,n,p) + binomial(6,n,p)

print round(ans, 3)