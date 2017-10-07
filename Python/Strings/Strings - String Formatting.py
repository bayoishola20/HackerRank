def print_formatted(number):
    # your code goes here
    space = len("{0:b}".format(n))
    for i in xrange(1,n+1):
        print "{0:{space}} {0:{space}o} {0:{space}X} {0:{space}b}".format(i,space=space)