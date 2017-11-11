cube = lambda x: x ** 3 # complete the lambda function 

def fibonacci(n):
    # return a list of fibonacci numbers
    seq = []
    for i in range(n):
        if i <= 1:
            seq.append(i)
        else:
            seq.append(seq[i - 2] + seq[i - 1])
    return list(seq)

#================================#
        # Code in stub #
#================================#
if __name__ == '__main__':
    n = int(raw_input())
    print map(cube, fibonacci(n))
