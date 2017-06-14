def print_rangoli(size):
    # your code goes here
    thickness = (n * 4) - 3
    
    #above the middle <--- This block needs to come first
    for i in xrange(n - 1):
        top = ("-").join(chr(ord('a') + n - j - 1) for j in xrange(i + 1))
        print (top + top[::-1][1:]).center(thickness, '-')
        
        
    mid = ("-").join(chr(ord('a') + n - i - 1) for i in xrange(n))
    print (mid + mid[::-1][1:]).center(thickness, '-')
    
    #below the middle <--- This block needs to come last
    for i in xrange(n - 1):
        bottom = ("-").join(chr(ord('a') + n - j - 1) for j in xrange(n - i - 1))
        print (bottom + bottom[::-1][1:]).center(thickness, '-')

#==================== GIVEN CODE ======================#
if __name__ == '__main__':
    n = int(raw_input())
    print_rangoli(n)
#===================== END =========================#