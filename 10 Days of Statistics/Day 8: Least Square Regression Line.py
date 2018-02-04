x = [95, 85, 80, 70, 60] #list(map(float, raw_input().split()))
y = [85, 95, 70, 65, 70] #list(map(float, raw_input().split()))

mean_x = sum(x)/len(x)
mean_y = sum(y)/len(y)

xy = 0
x_square = 0

for i in xrange(len(x)):
    x_square += x[i] ** 2

for i in xrange(len(x)):
    xy += x[i]*y[i]

b = (len(x) * xy - sum(x) * sum(y)) / float(len(x) * x_square - (sum(x) ** 2))
a = mean_y - b * mean_x


print round(a + 80 * b, 3)x = [95, 85, 80, 70, 60] #list(map(float, raw_input().split()))
y = [85, 95, 70, 65, 70] #list(map(float, raw_input().split()))

mean_x = sum(x)/len(x)
mean_y = sum(y)/len(y)

xy = 0
x_square = 0

for i in xrange(len(x)):
    x_square += x[i] ** 2

for i in xrange(len(x)):
    xy += x[i]*y[i]

b = (len(x) * xy - sum(x) * sum(y)) / float(len(x) * x_square - (sum(x) ** 2))
a = mean_y - b * mean_x


print round(a + 80 * b, 3)