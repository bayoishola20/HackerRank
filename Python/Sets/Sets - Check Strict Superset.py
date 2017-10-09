A = set(raw_input().split())
n = int(raw_input())
strict = True
for i in xrange(n): 
    S = set(raw_input().split())
    strict = strict and A.issuperset(S)
print strict