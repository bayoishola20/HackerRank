N = int(raw_input())
X = list(int(x) for x in raw_input().split())
W = list(int(x) for x in raw_input().split())


print round(sum([X[i] * W[i] for i in xrange(N)])/float(sum(W)), 1)