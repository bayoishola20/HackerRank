//Write your code here
class Calculator: public AdvancedArithmetic {
    int divisorSum(int n) {
        int sum = 0;
        for (int i = 1; i <= n; i++) {
            if (n % i == 0)
                sum += i;
        }
        return sum;
    }
};

// This was not the plan. No python test-case for this.