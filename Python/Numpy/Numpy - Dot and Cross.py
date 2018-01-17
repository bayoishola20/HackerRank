import numpy
N = int(raw_input())
A = numpy.array([list(map(int, raw_input().split())) for n in xrange(N)])
B = numpy.array([list(map(int, raw_input().split())) for n in xrange(N)])

print numpy.dot(A, B)