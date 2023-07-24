class Operand:
    def __init__(self, raw_num):
        self.nUmber = int(raw_num)
 #      return Operand(self.nUmber + other)
    def method_1(self):
        return (self.nUmber)

class Operator:
    def __init__(self, raw_opr):
        self.oPerator = raw_opr
    def method_2(self):
        return self.oPerator

class Operation:
    def __init__(self, x, y):
        self.addition = Operand(num1).method_1() + Operand(num2).method_1()
        self.substraction = Operand(num1).method_1() - Operand(num2).method_1()
        self.multiplication = Operand(num1).method_1() * Operand(num2).method_1()
        self.division = Operand(num1).method_1() / Operand(num2).method_1()
    def manipulation(self):
       if (Operator(symbol).method_2()) in ["+","plus","add"]:
           return self.addition
       if (Operator(symbol).method_2()) in ["-","minus","substract"]:
           return self.substraction
       if (Operator(symbol).method_2()) in ["*","x","times"]:
           return self.multiplication
       if (Operator(symbol).method_2()) in ["/",":","divide"]:
           return self.division

class Result:
   def __init__(self):
       self.show = Operation(num1,num2).manipulation()
   def realshow(self):
       print (self.show)

# input operand like 8, eight, "one" etc.
num1 = input(f'enter a number: ') # be input by user
#operand1 = Operand(num1)
#print(type(num1))
#print(Operand(num1))
#print(type(Operand(num1)))
#print(Operand.method_1(num1))
#print(type(Operand.method_1(num1)))
#print(Operand(num1).method_1())
#print(type(Operand(num1).method_1()))
#print(type(operand1))

# input operand like 8, eight, "one" etc.
num2 = input("enter one more number: ") # be input by user
#operand2 = Operand(num2)
#print (operand2.method_1())

# operator like * x : / + -, divide, add , multiply etc.
symbol = input('enter operator: ') #be input by user
#print (operator.method_2())
"""
print(Operator(symbol))
print(Operator(symbol).method_2())
print(type(Operator(symbol)))
print(type(Operator(symbol).method_2()))
"""

#print (Operation(num1,num2).manipulation())
#or
Output = Result().realshow()

# Result of the operation
#result = Operation()
#if (operator.method_2() in ["*","x","time"]):
#    print (result.multiplication(operand1.method_1(),operand2.method_1()))
#if (operator.method_2() in ["/",":","divide"]):
#    print (result.division(operand1.method_1(),operand2.method_1()))
#if (operator.method_2() in ["+","plus","add"]):
#    print (result.addition(operand1.method_1(),operand2.method_1()))
#if (operator.method_2() in ["-","minus","substract"]):
#    print (result.substraction(operand1.method_1(),operand2.method_1()))