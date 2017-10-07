if __name__ == '__main__':
    N = int(raw_input())
    arr = []
    for i in xrange(0, N):
        items = raw_input().split()
        command = items[0]
        if command == 'insert':
            arr.insert(int(items[1]), int(items[2]))
        elif command == 'remove':
            arr.remove(int(items[1]))
        elif command == 'append':
            arr.append(int(items[1]))
        elif command == 'sort':
            arr.sort()
        elif command == 'pop':
            arr.pop()
        elif command == 'reverse':
            arr.reverse()
        else:
            print arr