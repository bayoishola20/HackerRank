import math
S = int(raw_input()) #sample size
mean = float(raw_input())
std = float(raw_input())
dist = float(raw_input())
z = float(raw_input())

def central_limit(S, std, z):
    return z * (std / math.sqrt(S))


print round(mean - central_limit(S, std, z), 2)
print round(mean + central_limit(S, std, z), 2)