#==================== GIVEN ======================#
class Difference:
    def __init__(self, a):
        self.__elements = a
#===================== END =========================#

	# Add your code here
    def computeDifference(self):
        maximumDifference = 0 #bearest absolute possibility
        
        for i in xrange(0, len(a)):
            for j in xrange(0, len(a)):
                absolute_value = abs(a[i] - a[j])
                if absolute_value > maximumDifference:
                    maximumDifference = absolute_value
        self.maximumDifference = maximumDifference

#==================== GIVEN ======================#
# End of Difference class

_ = raw_input()
a = [int(e) for e in raw_input().split(' ')]

d = Difference(a)
d.computeDifference()

print d.maximumDifference
#===================== END =========================#