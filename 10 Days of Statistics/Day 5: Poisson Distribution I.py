mean = float(raw_input())
k = float(raw_input())
e = 2.71828 #constant

def factorial(n):
    if n > 1:
        return factorial(n - 1) * n
    if n == 1 or n == 0:
        return 1

ans = ((mean ** k) * (e ** (-mean))) /  factorial(k)

print round(ans, 3)