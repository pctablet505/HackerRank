def divisorSum(self, n):
    pass


class Calculator(AdvancedArithmetic):
    def divisorSum(self, n):
        res = 0
        for i in range(1, n + 1):
            if n % i == 0:
                res += i
        return res
