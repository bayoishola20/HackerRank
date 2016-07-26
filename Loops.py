Python 2.7.9 (default, Apr  2 2015, 15:33:21) 
[GCC 4.9.2] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> #!/bin/python

import sys


N = int(raw_input().strip())
for i in range(1,11):
	result = N*i
	print '%s x %s = %d' %(N, i, result)
	
>>> 
