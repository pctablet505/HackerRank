class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, other):
        return Complex((self.real + other.real), (self.imaginary + other.imaginary))

    def __sub__(self, other):
        return Complex((self.real - other.real), (self.imaginary - other.imaginary))

    def __mul__(self, other):
        return Complex((self.real * other.real - self.imaginary * other.imaginary),
                       (self.imaginary * other.real + self.real * other.imaginary))

    def __truediv__(self, other):
        a = self.real
        b = self.imaginary
        c = other.real
        d = other.imaginary
        return Complex((a * c + b * d) / (c ** 2 + d ** 2), (b * c - a * d) / (c ** 2 + d ** 2))

    def mod(self):
        return Complex(((self.real ** 2 + self.imaginary ** 2) ** 0.5), 0)

    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result
