from sklearn import linear_model

m, n = map(int, raw_input().split())
X = list()
Y = list()

# Get X and Y for variables a and b
for i in xrange(n):
    x = [0]
    values = list(map(float, raw_input().split()))
    for j in xrange(len(values)):
        if j < m:
            x.append(values[j])
        else:
            Y.append(values[j])
    X.append(x)

# Linear regression model
model = linear_model.LinearRegression()
model.fit(X, Y)
a = model.intercept_
b = model.coef_

# parameters X for finding the Y
q = int(raw_input())
X_change = []
for i in xrange(q):
    x = [0]
    values = list(map(float, raw_input().split()))
    for j in xrange(len(values)):
        x.append(values[j])
    X_change.append(x)


ans = model.predict(X_change)
for i in xrange(len(ans)):
    print(round(ans[i],2))