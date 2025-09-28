class Complex:
    def __init__(self , real ,imag):
        self.real  = real 
        self.imag = imag
    
    def showNum(self):
        print(self.real,"i +",self.imag,"j")

    def __add__(self , num2 ):
        newReal = self.real + num2.real
        newimag = self.imag + num2.imag
        return Complex(newReal , newimag)

Num1=Complex(1,3)
Num1.showNum()    

Num2=Complex(2,5)
Num2.showNum()

num3 = Num1 + Num2
num3.showNum()