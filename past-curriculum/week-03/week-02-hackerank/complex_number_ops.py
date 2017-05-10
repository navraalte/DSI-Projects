class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary
        
    def __add__(self, no):
        self.real_add = self.real + no.real
        self.imag_add = self.imaginary + no.imaginary
        self.sum = Complex(self.real_add,self.imag_add)
        return str(self.sum)

    def __sub__(self, no):
       
        self.real_sub = self.real - no.real
        self.imag_sub = self.imaginary - no.imaginary
        self.diff = Complex(self.real_sub,self.imag_sub)
        return str(self.diff)
        
        
    def __mul__(self, no):
        self.real_mul = (self.real*no.real -self.imaginary*no.imaginary)
        self.imag_mul = (self.real*no.imaginary+no.real*self.imaginary)
        self.prod = Complex(self.real_mul,self.imag_mul)
        return str(self.prod)


    def __div__(self, no):
        self.real_div = float(float(self.real*no.real+self.imaginary*no.imaginary)/float(no.real*no.real+no.imaginary*no.imaginary))
        self.imag_div = float(float(no.real*self.imaginary-self.real*no.imaginary)/float(no.real*no.real+no.imaginary*no.imaginary))
        self.quo = Complex(self.real_div,self.imag_div)
        return str(self.quo)
        
        
    def mod(self):
        self.modulo = math.sqrt(self.real ** 2 + self.imaginary **2 )
        return Complex(round(self.modulo,2),0)

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
