class Operand:
    def __init__(self, raw_num):
        self.nUmber = float(raw_num)
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
        if Operand(num2).method_1() != 0:
            self.division = Operand(num1).method_1() / Operand(num2).method_1()
    def manipulation(self):
        match Operator(symbol).method_2():
            case "+"| "plus"| "add":
                return self.addition
            case "-"|"minus"|"substract":
                return self.substraction
            case "*"|"x"|"times":
                return self.multiplication
            case "/"|":"|"divide":
                return self.division

class Result:
   def __init__(self):
       self.show = Operation(num1,num2).manipulation()
   def realshow(self):
       print (self.show)

class exception:
    pass

# input operand like 8, eight, "one" etc.
num1 = input(f'enter a number: ') # be input by user

# input operand like 8, eight, "one" etc.
num2 = input("enter one more number: ") # be input by user

# operator like * x : / + -, divide, add , multiply etc.
symbol = input('enter operator, I accept all these ["+","plus","add"]\n["-","minus","substract"]\n["*","x","times"]\n["/",":","divide"]: ') #be input by user

# Result :
Output = Result().realshow()

