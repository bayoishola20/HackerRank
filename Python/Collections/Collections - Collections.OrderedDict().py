# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict
N = int(raw_input())
items = OrderedDict()

for i in xrange(N):
    item_name, space, qty = raw_input().rpartition(' ') #Split the string by space, and return a 3-tuple
    items[item_name] = items.get(item_name, 0) + int(qty)
for item_name, qty in items.items():
    print item_name, qty