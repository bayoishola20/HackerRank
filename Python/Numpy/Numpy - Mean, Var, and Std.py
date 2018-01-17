import numpy
N, M = map(int, raw_input().split())

array = numpy.array([list(map(int, raw_input().split())) for _ in xrange(N)])

print numpy.mean(array, axis = 1)
print numpy.var(array, axis = 0)
print numpy.std(array, axis = None)