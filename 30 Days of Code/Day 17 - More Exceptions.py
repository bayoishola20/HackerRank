#Write your code here
class Calculator():
    def power(self, n, p):
        self.n = n
        self.p = p
        if n < 0 or p < 0: #checking for negativity
            return "n and p should be non-negative"
        return pow(n, p)

#==================== GIVEN ======================#
myCalculator=Calculator()
T=int(raw_input())
for i in range(T):
    n,p = map(int, raw_input().split())
    try:
        ans=myCalculator.power(n,p)
        print ans
    except Exception,e:
        print e
#===================== END =========================#