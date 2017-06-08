class Calculator(AdvancedArithmetic):
    def divisorSum(self, n):
        self.n = n
        sum = 0
        for i in xrange(n):
            if n % i == 0:
                sum += i
        return sum

'''

This was blind-coded. No test cases available.

'''
