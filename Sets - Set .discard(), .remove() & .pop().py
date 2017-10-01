n = input()
s = set(map(int, raw_input().split())) 
N = int(raw_input())

for i in xrange(N):
    cmd = raw_input().split()
    if cmd[0] == 'pop':
        s.pop()
    if cmd[0] == 'remove':
        s.remove(int(cmd[1]))
    if cmd[0] == 'discard':
        s.discard(int(cmd[1]))

print sum(s)