def wrapper(f):
    def fun(l):
        # complete the function
        return f(["+91" + " " + i[-10:-5] + " " + i[-5:] for i in l])
    return fun

#===============================#
    # Code in stub below #
#===============================#

@wrapper
def sort_phone(l):
    print '\n'.join(sorted(l))

if __name__ == '__main__':
    l = [raw_input() for _ in range(int(input()))]
    sort_phone(l) 