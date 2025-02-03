class Calculator:
    brand ='Casio MS990'
    def add(self,num1,num2):
        sum = num1+num2
        return sum
    def mult(self,num1,num2):
        m = num1*num2
        n = num1//num2
        return m,n

addition = Calculator()
addi = addition.add(1,2)
print(addi)
mul = addition.mult(2,3)
print(mul)
#deduct methon

#multiply method

#devide method