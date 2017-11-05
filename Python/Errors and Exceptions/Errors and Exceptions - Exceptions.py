T = int(raw_input().strip())

for _ in xrange(T):
    try:
        a, b = map(int, raw_input().split())
        print a/b
    except ZeroDivisionError as x:
        print "Error Code:", x
    except ValueError as x:
        print "Error Code:", x