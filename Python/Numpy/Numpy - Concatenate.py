import numpy
N, M, P = map(int, raw_input().split())

array_1 = numpy.array( [list(map(int, raw_input().split())) for _ in range(N)] )
array_2 = numpy.array( [list(map(int, raw_input().split())) for _ in range(M)] )

print numpy.concatenate((array_1, array_2), axis = 0)