N = int(raw_input())
X = list(map(int, raw_input().split()))

def quartiles(X): #median or q2
    X = sorted(X)
    total = len(X)
    
    if total % 2:
        return int(X[total/2])
    else:
        return sum(X[(total/2-1):(total/2+1)])/2

if N == 1:
    print X[0]
    print X[0]
    print X[0]
    
else:
    odd = N % 2
    X = sorted(X)        

    print quartiles(X[:N/2]) #q1
    print quartiles(X) #q2
    print quartiles(X[N/2 + 1 if odd else N/2:]) #q3