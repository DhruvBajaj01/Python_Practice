class complex:
    def __init__(self,real,imaginary):
        self.real=real
        self.imaginary= imaginary

    def __add__(self,num2):
        return complex(self.real + num2.real , self.imaginary + num2.imaginary)

    def __mul__(self,num2):
        realPart= self.real*num2.real - self.imaginary*num2.imaginary
        imaginary= self.real*num2.imaginary + self.imaginary*num2.real
        return complex(realPart , imaginary)

    def __str__(self):
        return (f"{self.real} + {self.imaginary}i")




n1= complex(3,2)
n2= complex(1,7)
sum = n1+n2
print(sum)
multiply= n1*n2
print(multiply)
