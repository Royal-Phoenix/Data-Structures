class Queue:
    def __init__(self):
        self.queue = []
        
    def Enqueue(self):
        data = int(input("Enter the Value to Enqueue : "))
        self.queue.append(data)

    def Dequeue(self):
        del self.queue[0]
        print("Queue Elements after Dequeuing")

    def Peek(self):
        print("Front Element of the Queue is",self.queue[0])

    def Search(self):
        data = int(input("Enter the Value to Search : "))
        print("Position of",data,"from Front is ",end = "")
        print(self.queue.index(data)+1)

    def Empty(self):
        if len(self.queue)==0:
            print("Queue is Empty")
        else:
            print("Queue is not Empty")
    
    def Display(self):
        l = len(self.queue)
        print(" ______" * l)
        print("|      " * l)
        for i in self.queue:
            print("| ",i," ",end = "")
        print()
        print("|______" * l)

obj = Queue()
obj.Enqueue()
obj.Enqueue()
obj.Enqueue()
obj.Enqueue()
obj.Display()
obj.Peek()
obj.Dequeue()
obj.Display()
obj.Search()
obj.Dequeue()
obj.Display()
