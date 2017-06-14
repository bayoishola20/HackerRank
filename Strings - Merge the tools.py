def merge_the_tools(string, k):
    # your code goes here
    s = string.strip()
    u = len(s)//k #length of subsegment
    
    for i in xrange(u):
        x = ''
        for j in s[i*k:i*k+k]:
            if j not in x:
                x += j
        print x

#==================== GIVEN CODE ======================#
if __name__ == '__main__':
    string, k = raw_input(), int(raw_input())
    merge_the_tools(string, k)
#===================== END =========================#