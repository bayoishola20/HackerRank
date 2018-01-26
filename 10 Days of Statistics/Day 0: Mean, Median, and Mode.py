import numpy
from scipy import stats
N = int(raw_input())
X = list(map(int, raw_input().split()))

print numpy.mean(X)
print numpy.median(X)
print int(stats.mode(X)[0])