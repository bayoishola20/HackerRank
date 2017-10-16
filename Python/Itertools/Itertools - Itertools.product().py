# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product
A = map(int, raw_input().strip().split())
B = map(int, raw_input().strip().split())

print ' '.join(map(str, product(A, B)))