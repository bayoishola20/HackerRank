from collections import Counter
X = int(raw_input())
myList = list(map(int, raw_input().split()))
shoes = Counter(myList)
N = int(raw_input())

earning = 0
for i in xrange(N):
    size, price = map(int, raw_input().split())
    if shoes[size] > 0:
        earning += price
        shoes[size] -= 1
print earning