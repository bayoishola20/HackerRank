#==================== GIVEN CODE ======================#
if __name__ == '__main__':
    x = int(raw_input())
    y = int(raw_input())
    z = int(raw_input())
    n = int(raw_input())
s#===================== END =========================#
    
    ans = []
    [ans.append([x,y,z]) for x in xrange(0, x+1) for y in xrange(0, y+1) for z in xrange(0, z+1) if x + y + z !=n]
    
    print ans