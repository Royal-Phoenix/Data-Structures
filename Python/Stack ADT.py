class Stack:
    def __init__(self):
        self.stack = []
        
    def Push(self):
        data = int(input("Enter the Value to Push : "))
        self.stack.append(data)

    def Pop(self):
        self.stack.pop()
        print("Stack Elements after Popping")

    def Peek(self):
        print("Top Element of the Stack is",self.stack[-1])

    def Search(self):
        data = int(input("Enter the Value to Search : "))
        print("Position of",data,"from Top is ",end = "")
        print(len(self.stack)-self.stack.index(data))

    def Empty(self):
        if len(self.stack)==0:
            print("Stack is Empty")
        else:
            print("Stack is not Empty")
    
    def Display(self):
        l = len(self.stack)
        for i in range(l-1,-1,-1):
            print("|      |")
            print("| ",self.stack[i]," |")
            print("|______|")

obj = Stack()
obj.Push()
obj.Push()
obj.Push()
obj.Push()
obj.Display()
obj.Peek()
obj.Pop()
obj.Display()
obj.Search()
obj.Pop()
obj.Display()
