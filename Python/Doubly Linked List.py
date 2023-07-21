class Node:
    def __init__(self, data):
       self.data = data
       self.prev = None
       self.next = None
 
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def Create(self):
        n = int(input("Enter the Number of Elements : "))
        for i in range(n):
            data = int(input("Enter an Element : "))
            self.Insert_End(data)
    
    def Display(self):
        temp = self.head
        while temp:
            print("<-->",temp.data,end = " ")
            temp = temp.next
        print("<-->")
    
    def Insert_Beg(self,data):
        new = Node(data)
        new.next = self.head
        self.head.prev = new
        new.prev = None
        self.head = new
    
    def Insert_Mid(self,pos,data):
        new = Node(data)
        temp = self.head
        for i in range(pos-1):
            temp = temp.next
        new.next = temp.next
        temp.next = new
        new.prev = temp
        new.next.prev = new
    
    def Insert_End(self,data):
        new = Node(data)
        if self.head is None:
            new.prev = None
            self.head = new
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new
            new.prev = temp
            self.tail = new
    
    def Delete_Beg(self):
        temp = self.head.next
        self.head.next = None
        self.head = temp
        temp.prev = None
    
    def Delete_Mid(self,pos):
        temp = self.head.next
        cur = self.head
        for i in range(1,pos):
            temp = temp.next
            cur = cur.next
        cur.next = temp.next
        temp.next.prev = cur
        temp.prev = None
        temp.next = None
    
    def Delete_End(self):
        temp = self.head.next
        cur = self.head
        while temp.next:
            temp = temp.next
            cur = cur.next
        temp.prev = None
        cur.next = None

obj = DoublyLinkedList()
obj.Create()
obj.Display()
print("Doubly Linked List Creation\n")
obj.Insert_Beg(20)
obj.Display()
print("Doubly Linked List Insertion at Beginning\n")
obj.Insert_Mid(3,30)
obj.Display()
print("Doubly Linked List Insertion at Middle at Position 3\n")
obj.Insert_End(40)
obj.Display()
print("Doubly Linked List Insertion at End\n")
obj.Delete_Beg()
obj.Display()
print("Doubly Linked List Deletion at Beginning\n")
obj.Delete_Mid(2)
obj.Display()
print("Doubly Linked List Deletion at Middle at Position 2\n")
obj.Delete_End()
obj.Display()
print("Doubly Linked List Deletion at End")
