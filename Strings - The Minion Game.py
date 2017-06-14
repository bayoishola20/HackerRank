def minion_game(string):
    # your code goes here
    vowels = ('A', 'E', 'I', 'O', 'U')
    Kevin = 0
    Stuart = 0
    for i in xrange(len(s)):
        if s[i] in vowels:
            Kevin += len(s) - i
        elif s[i] not in vowels:
            Stuart += len(s) - i
    if Kevin > Stuart:
        print 'Kevin', Kevin
    elif Kevin < Stuart:
        print 'Stuart', Stuart
    else:
        print "Draw"

#==================== GIVEN CODE ======================#
if __name__ == '__main__':
    s = raw_input()
    minion_game(s)
#===================== END =========================#