import numpy
N, M = numpy.array(raw_input().strip().split(), int)
print numpy.eye(N, M, k = 0)