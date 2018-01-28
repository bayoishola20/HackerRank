import math

N = int(raw_input())
X = list(map(int, raw_input().split()))

def calc_mean(X):
    return sum(X)/float(len(X))


mean = calc_mean(X)

print float(math.sqrt(calc_mean([(i - mean)**2 for i in X])))