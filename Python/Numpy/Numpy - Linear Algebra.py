import numpy
N =int(raw_input())

A = numpy.array([list(map(float, raw_input().split())) for _ in xrange(N)])


print numpy.linalg.det(A)