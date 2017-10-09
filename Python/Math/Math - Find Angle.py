# Enter your code here. Read input from STDIN. Print output to STDOUT
import cmath, math
AB = int(raw_input())
BC = int(raw_input())

angleMBC = int(round(math.degrees(cmath.phase(complex(0, AB) + complex(0, 0) + complex(BC, 0)))))
print str(angleMBC) + "°"