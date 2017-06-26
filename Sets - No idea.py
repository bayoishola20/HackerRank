# Enter your code here. Read input from STDIN. Print output to STDOUT
n,m = (i for i in raw_input().split(' '))
n = map(int, raw_input().split())
A = set(map(int, raw_input().split()))
B = set(map(int, raw_input().split()))
h = 0 #h for happiness
for i in n:
    if i in A:
        h += 1
    elif i in B:
        h -= 1
print h