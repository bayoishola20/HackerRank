if __name__ == '__main__':
    n = int(raw_input())
    integer_list = map(int, raw_input().split())
    t = (integer_list[0], )
    for i in xrange(1, n):
        t += (integer_list[i],)
    print hash(t)