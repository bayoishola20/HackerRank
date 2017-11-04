from collections import OrderedDict
n = int(raw_input())
ordered_dict = OrderedDict()
for i in xrange(n):
    words = str(raw_input())
    ordered_dict[words] = ordered_dict.get(words,0) + 1
print len(ordered_dict)
for j in ordered_dict.values():
    print j,