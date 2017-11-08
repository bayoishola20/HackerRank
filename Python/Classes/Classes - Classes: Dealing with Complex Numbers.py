class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary
        
    def __add__(self, no):
        real = self.real + no.real
        imaginary = self.imaginary + no.imaginary
        return Complex(real, imaginary)

    def __sub__(self, no):
        real = self.real - no.real
        imaginary = self.imaginary - no.imaginary
        return Complex(real, imaginary)
        
    def __mul__(self, no):
        real = self.real * no.real - self.imaginary * no.imaginary
        imaginary = self.imaginary * no.real + self.real * no.imaginary
        return Complex(real, imaginary)

    def __div__(self, no):
        real = (self * Complex(no.real, -no.imaginary)).real / float(no.real ** 2 + no.imaginary ** 2)
        imaginary = (self * Complex(no.real, -no.imaginary)).imaginary / float(no.real ** 2 + no.imaginary ** 2)
        return Complex(real, imaginary)
        
    def mod(self):
        real = (self.real**2 + self.imaginary**2)**0.5
        return Complex(real, 0)

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

#############################################
           # Code stub #
#############################################
if __name__ == '__main__':
    c = map(float, raw_input().split())
    d = map(float, raw_input().split())
    x = Complex(*c)
    y = Complex(*d)
    print '\n'.join(map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]))