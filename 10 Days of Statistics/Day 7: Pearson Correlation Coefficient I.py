import math
N = int(raw_input())
X = list(map(float, raw_input().split()))
Y = list(map(float, raw_input().split()))

def mean(X):
    x = 0
    for i in X:
        x += i
    return x/len(X)

def std(X):
    x = 0
    for i in X:
        x += (i - mean(X))**2
    return math.sqrt(x/len(X))

def corr_coeff(N, X, Y):
    mean_X = mean(X)
    std_X = std(X)
    mean_Y = mean(Y)
    std_Y = std(Y)
    ans = 0
    for i in xrange(N):
        ans = ans + (X[i]-mean_X) * (Y[i]-mean_Y)
    return ans/(N * std_X * std_Y)

print round(corr_coeff(N, X, Y), 3)