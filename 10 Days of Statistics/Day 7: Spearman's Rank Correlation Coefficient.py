N = int(raw_input())
X = list(map(float, raw_input().split()))
Y = list(map(float, raw_input().split()))

def rank(X):
    rank = dict()
    for i in xrange(len(X)):
        for j in xrange(len(sorted(X))):
            if X[i] == sorted(X)[j]:
                rank[X[i]] = j + 1
    return rank

def spear_corr_coeff(X, Y, rank_X, rank_Y, N):
    rank_diff = 0
    for i in xrange(N):
        if rank_X[X[i]] != rank_Y[Y[i]]:
            rank_diff = rank_diff + (rank_X[X[i]] - rank_Y[Y[i]]) ** 2
    return 1 - ((6 * rank_diff) / float(N ** 3 - N))

rank_X = rank(X)
rank_Y = rank(Y)

print round(spear_corr_coeff(X, Y, rank_X, rank_Y, N), 3)