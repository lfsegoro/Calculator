class Operand:
    def __init__(self, raw_num):
        self.nUmber = raw_num
    def method_1(self):
        return int(self.nUmber)

class Operator:
    def __init__(self, raw_operator):
        self.oPerator = raw_operator
    def method_2(self):
        return self.oPerator

class Operation:
    def addition(self, operand1, operand2):
        return operand1 + operand2
    def substraction(self, operand1, operand2):
        return operand1 - operand2
    def multiplication(self, operand1, operand2):
        return operand1 * operand2
    def division(self, operand1, operand2):
        return operand1 / operand2

# input operand like 8, eight, "one" etc.
num1 = input(f'enter a number: ') # be input'ed by user
operand1 = Operand(num1)
#print(type(operand1.method_1()))
#print(type(operand1))

# input operand like 8, eight, "one" etc.
num2 = input("enter one more number: ") # be input'ed by user
operand2 = Operand(num2)
#print (operand2.method_1())

# operator like * x : / + -, divide, add , multiply etc.
symbol = input('enter operator: ') #be input'ed by user
operator = Operator(symbol)
#print (operator.method_2())

# Result of the operation
result = Operation()
if (operator.method_2() in ["*","x","time"]):
    print (result.multiplication(operand1.method_1(),operand2.method_1()))
if (operator.method_2() in ["/",":","divide"]):
    print (result.division(operand1.method_1(),operand2.method_1()))
if (operator.method_2() in ["+","plus","add"]):
    print (result.addition(operand1.method_1(),operand2.method_1()))
if (operator.method_2() in ["-","minus","substract"]):
    print (result.substraction(operand1.method_1(),operand2.method_1()))