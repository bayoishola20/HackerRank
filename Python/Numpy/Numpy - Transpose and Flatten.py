import numpy
N, M = numpy.array(raw_input().strip().split(' '), int)

ans = []
for i in xrange(N):
    ans.append(raw_input().strip().split(' '))

result = numpy.reshape(numpy.array(ans, int), (N, M))

print numpy.transpose(result)
print result.flatten()