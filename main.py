#initialize global variables
num=[5,7]
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
        self.addition = Operand(num[0]).method_1() + Operand(num[1]).method_1()
        self.substraction = Operand(num[0]).method_1() - Operand(num[1]).method_1()
        self.multiplication = Operand(num[0]).method_1() * Operand(num[1]).method_1()
        if Operand(num[1]).method_1() != 0:
            self.division = Operand(num[0]).method_1() / Operand(num[1]).method_1()
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
       self.show = Operation(num[0],num[1]).manipulation()
   def realshow(self):
       print (self.show)

def invoke_console():
    global num1
    global num2
    global symbol
#Uncomment below if you want to use/activate console base calculator
# input operand like 8, eight, "one" etc.
    num[0] = float(input(f'enter a number: ')) # be input by user
# input operand like 8, eight, "one" etc.
    num[1] = float(input("enter one more number: ")) # be input by user
# operator like * x : / + -, divide, add , multiply etc.
    symbol = input('enter operator, I accept all these ["+","plus","add"]\n["-","minus","substract"]\n["*","x","times"]\n["/",":","divide"]: ') #be input by user
# Result :
    Result().realshow()

#======Above are console calculator, Below are GUI that also use above classes.
from tkinter import *
#from tkinter import ttk
root = Tk()
root.geometry('400x300')
root.title('Train Multiply for Children')
class Label_widget:
    def __init__(self,y,column,row):
        label = Label(root, font=("Ariel", 22), text=y)
        label.grid(column=column, row=row)
class Entry_generic:
    def __init__(self,column,row):
        self.entry = Entry(root, font=("Ariel", 22), width=5)
        self.entry.grid(column=column, row=row)
    def method(self,y):
        self.entry.insert(0,y)
#class for entry widget creation, also re-assignment num[0] and num[1]
class Entry_widget(Entry_generic):
    def __init__(self,column,row):
        #nvm..Anyone know how to inherite this class from above 'Entry_generic', i.e how to implement super(), when I try, the entry insert become stacked looks like 2 times executed.
        super().__init__(column,row)
        #self.entry = Entry(root, font=("Ariel", 22), width=5)
        #self.entry.grid(column=column, row=row)
    def method(self,y):
        self.entry.insert(0,num[int(y)])
        #self.entry.bind("<Leave>", lambda event: exec('num[' + y + ']=' + self.entry.get(), globals()))
        self.entry.bind("<Expose>", lambda event:exec('num[' + y + ']=' + self.entry.get(), globals()))
        self.entry.bind("<KeyRelease>", lambda event:exec('num[' + y + ']=' + self.entry.get(), globals()))
class Button_widget:
    def __init__(self,i,x,y,column,row):
        # 2 lines below: a variable that only need a ride:)
        global symbol
        symbol = Operator(y).method_2()
        self.button = Button(root, text=x, width=8)
        self.button.grid(column=column, row=row)
        if i == 6:
            self.button.bind("<Button-1>", lambda eve: invoke_console())
            return
        self.button.bind("<ButtonRelease-1>", lambda event:self.buttonclick(i,y))
    def buttonclick(self,i,y):
        global symbol
        symbol = Operator(y).method_2()
        match i:
            case 1:
                num[0]=num[0]+1
                Entry_widget(0,1).method('0')
            case 2:
                num[0]=num[0]-1
                Entry_widget(0,1).method('0')
            case 3:
                num[1]=num[1]+1
                Entry_widget(2,1).method('1')
            case 4:
                num[1]=num[1]-1
                Entry_widget(2,1).method('1')
            case 5:
                pass
        Entry_generic(1,4).method(Operation(num[0],num[1]).manipulation())
Entry_widget(0,1).method('0')
Entry_widget(2,1).method('1')
#All 5 lines below there operator for demonstration I use "x",'*' and 'times'.
Button_widget(1,'UP','x',0,0)
Button_widget(2,'DOWN','*',0,2)
Button_widget(3,'UP','times',2,0)
Button_widget(4,'DOWN','*',2,2)
Button_widget(5,'=','*',1,3)
Entry_generic(1,4).method(Operation(num[0],num[1]).manipulation())
Button_widget(6,'Console','*',1,5)
Label_widget('X',1,1)
root.mainloop()