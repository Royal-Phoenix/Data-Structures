class Node:
    def __init__(self, data):
       self.data = data
       self.next = None
 
class CircularlyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.nodes = 0
    
    def Create(self):
        n = int(input("Enter the Number of Elements : "))
        for i in range(n):
            data = int(input("Enter an Element : "))
            self.Insert_End(data)
    
    def Display(self):
        temp = self.head
        for i in range(self.nodes):
            print(temp.data,"-->",end = " ")
            temp = temp.next
        print()
        
    def Insert_Beg(self,data):
        self.nodes += 1
        new = Node(data)
        temp = self.head
        new.next = temp
        self.head = new
        self.tail.next = new
            
    def Insert_Mid(self,pos,data):
        self.nodes += 1
        new = Node(data)
        temp = self.head
        for i in range(pos):
            cur = temp
            temp = temp.next
        cur.next = new
        new.next = temp
            
    def Insert_End(self, data):
        self.nodes += 1
        new = Node(data)
        if self.head is None:
            self.head = new
            self.tail = new
        else:
            temp = self.head
            for i in range(self.nodes-2):
                temp = temp.next
            temp.next = new
            self.tail = new
            new.next = self.head
        
    def Delete_Beg(self):
        self.nodes -= 1
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.tail.next = self.head
 
    def Delete_Mid(self,pos):
        self.nodes -= 1
        temp = self.head.next
        prev = self.head
        for i in range(1,pos-1):
            temp = temp.next
            prev = prev.next
        prev.next = temp.next

    def Delete_End(self):
        self.nodes -= 1
        temp = self.head.next
        prev = self.head
        for i in range(self.nodes-1):
            temp = temp.next
            prev = prev.next
        prev.next = temp.next
        temp.next = None
        self.tail = prev
 
obj = CircularlyLinkedList()
obj.Create()
obj.Display()
print("Circular Linked List Creation\n")
obj.Insert_Beg(20)
obj.Display()
print("Circular Linked List Insertion at Beginning\n")
obj.Insert_Mid(3,30)
obj.Display()
print("Circular Linked List Insertion at Middle at Position 3\n")
obj.Insert_End(40)
obj.Display()
print("Circular Linked List Insertion at End\n")
obj.Delete_Beg()
obj.Display()
print("Circular Linked List Deletion at Beginning\n")
obj.Delete_Mid(2)
obj.Display()
print("Circular Linked List Deletion at Middle at Position 2\n")
obj.Delete_End()
obj.Display()
print("Circular Linked List Deletion at End")
