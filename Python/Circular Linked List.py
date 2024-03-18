class Node:
    def __init__(self, data):
       self.data, self.next = data, None
 
class CircularlyLinkedList:
    def __init__(self):
        self.head, self.tail, self.nodes = None, None, 0
    
    def insertStart(self, data):
        new = Node(data)
        if self.head is None:
            self.head, self.tail = new, new
        else:
            new.next = self.head
            self.head = new
            self.tail.next = new
        self.nodes += 1
    
    def insertMid(self, pos, data):
        if self.head is None:
            new = Node(data)
            self.head, self.tail = new, new
            self.nodes += 1
        else:
            if pos == 1:
                self.insertStart(data)
            elif pos >= self.nodes:
                self.insertEnd(data)
            else:
                new, temp = Node(data), self.head
                for _ in range(pos-2):
                    temp = temp.next
                new.next = temp.next
                temp.next = new
                self.nodes += 1
    
    def insertEnd(self, data):
        new = Node(data)
        if self.head is None:
            self.head, self.tail = new, new
        else:
            self.tail.next = new
            self.tail = new
            new.next = self.head
        self.nodes += 1
    
    def deleteStart(self):
        if self.head is None:
            return None
        else:
            temp = self.head
            self.head = self.head.next
            self.tail.next = self.head
            temp.next = None
            self.nodes -= 1
            return temp
    
    def deleteMid(self, pos):
        if self.head is None:
            return None
        else:
            if pos == 1:
                self.deleteStart()
            elif pos >= self.nodes:
                self.deleteEnd()
            else:
                curr, temp = self.head, self.head.next
                for i in range(pos-2):
                    curr, temp = curr.next, temp.next
                curr.next = temp.next
                temp.next = None
                self.nodes -= 1
                return temp
    
    def deleteEnd(self):
        if self.head is None:
            return None
        else:
            curr = self.head
            for i in range(self.nodes-2):
                curr = curr.next
            temp = curr.next
            curr.next = self.head
            self.tail = curr
            temp.next = None
            self.nodes -= 1
            return temp
    
    def display(self):
        temp = self.head
        for i in range(self.nodes):
            print(temp.data, end='-->')
            temp = temp.next
        print()
