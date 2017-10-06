# Enter your code here. Read input from STDIN. Print output to STDOUT
T = int(raw_input())



def prime(n):
    for i in xrange(2, int((n)**0.5)+1):
        if n % i is 0:
            return False
    return True

for _ in xrange(T):
    n = int(raw_input())
    if n >=2 and prime(n):
        print "Prime"
    else:
        print "Not prime"