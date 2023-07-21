class Node:
    def __init__(self, data):
       self.data = data
       self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def Create(self):
        n = int(input("Enter the Number of Elements : "))
        for i in range(n):
            data = int(input("Enter an Element : "))
            obj.Insert_End(data)
    
    def Display(self):
        if self.head is None:
            print("The Linked List is Empty")
        else:
            temp = self.head
            while temp:
                print(temp.data,"-->",end = "")
                temp = temp.next
            print()
    
    def Insert_Beg(self,data):
        new = Node(data)
        new.next = self.head
        self.head = new
    
    def Insert_Mid(self,pos,data):
        new = Node(data)
        temp = self.head
        for i in range(pos-1):
            temp = temp.next
        new.next = temp.next
        temp.next = new
    
    def Insert_End(self,data):
        new = Node(data)
        if self.head is None:
            self.head = new
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new
    
    def Delete_Beg(self):
        temp = self.head
        self.head = self.head.next
        temp.next = None
    
    def Delete_Mid(self,pos):
        temp = self.head.next
        prev = self.head
        for i in range(1,pos):
            temp = temp.next
            prev = prev.next
        prev.next = temp.next
    
    def Delete_End(self):
        temp = self.head.next
        prev = self.head
        while temp.next is not None:
            temp = temp.next
            prev = prev.next
        prev.next = None

obj = SinglyLinkedList()
obj.Create()
obj.Display()
print("Singly Linked List Creation\n")
obj.Insert_Beg(20)
obj.Display()
print("Singly Linked List Insertion at Beginning\n")
obj.Insert_Mid(3,30)
obj.Display()
print("Singly Linked List Inserion at Middle at Position 3\n")
obj.Insert_End(40)
obj.Display()
print("Singly Linked List Insertion at End\n")
obj.Delete_Beg()
obj.Display()
print("Singly Linked List Deletion at Beginning\n")
obj.Delete_Mid(2)
obj.Display()
print("Singly Linked List Deletion at Middle at Position 2\n")
obj.Delete_End()
obj.Display()
print("Singly Linked List Deletion at End")
