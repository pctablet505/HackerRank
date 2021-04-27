class Calculator:
    def power(self, a, b):
        if a < 0 or b < 0:
            raise ValueError('n and p should be non-negative')
        return a ** b
