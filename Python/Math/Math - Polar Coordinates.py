# Enter your code here. Read input from STDIN. Print output to STDOUT
import cmath
n = raw_input()
z = cmath.phase(complex(n))
r = abs(complex(n))
print r
print z