class Complex:
    def __init__(self,a, b):
        self.real = a
        self.imag = b
    def __add__(self,other):
        #return self.real + other.real, self.imag + other.imag 
        self.real = self.real + other.real
        self.imag += other.imag
        return(self)
Ob1 = Complex(1,2)
Ob2 = Complex(2,3)
Ob3 = Ob1 + Ob2
print(self.real + "+i" + other.imag)
