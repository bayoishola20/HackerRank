# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(raw_input())
set_1 = set(map(int, raw_input().split()))
N = int(raw_input())

for i in xrange(N):
    cmd = raw_input().split()
    set_2 = set(map(int, raw_input().split()))
    if cmd[0] == 'intersection_update':
        set_1.intersection_update(set_2)
    if cmd[0] == 'update':
        set_1.update(set_2)
    if cmd[0] == 'symmetric_difference_update':
        set_1.symmetric_difference_update(set_2)
    if cmd[0] == 'difference_update':
        set_1.difference_update(set_2)

print sum(set_1)