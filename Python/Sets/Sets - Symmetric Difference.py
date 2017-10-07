# Enter your code here. Read input from STDIN. Print output to STDOUT
M = int(raw_input())
Mx = set(map(int, raw_input().split()))

N = int(raw_input())
Nx = set(map(int, raw_input().split()))

for i in sorted((Mx.difference(Nx)).union(Nx.difference(Mx))):
    print i