from collections import namedtuple
N = int(raw_input())
Student = namedtuple('Student',raw_input().strip().split())
print sum(float(i.MARKS) for i in ([Student(*raw_input().split()) for i in xrange(N)]))/N