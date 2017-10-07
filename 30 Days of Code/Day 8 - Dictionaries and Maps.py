n = int(raw_input())
phoneBook = dict(raw_input().split() for x in range(n))
for i in range(n):
    s = raw_input()
    try:
        print s+"="+phoneBook[s] 
    except:
        print 'Not found'