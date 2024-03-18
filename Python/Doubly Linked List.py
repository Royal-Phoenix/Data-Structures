class Node:
    def __init__(self, data):
       self.data, self.prev, self.next = data, None, None
 
class DoublyLinkedList:
    def __init__(self):
        self.head, self.tail, self.nodes = None, None, 0
    
    def insertStart(self, data):
        new = Node(data)
        if self.head is None:
            self.head, self.tail = new, new
        else:
            new.next = self.head
            self.head.prev = new
            self.head = new
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
                new = Node(data)
                curr, temp = self.head, self.head.next
                for _ in range(pos-2):
                    curr, temp = curr.next, temp.next
                curr.next = new
                new.prev = curr
                new.next = temp
                temp.prev = new
                self.nodes += 1
    
    def insertEnd(self, data):
        new = Node(data)
        if self.head is None:
            self.head, self.tail = new, new
        else:
            self.tail.next = new
            new.prev = self.tail
            self.tail = new
        self.nodes += 1
    
    def deleteStart(self):
        if self.head is None:
            return None
        else:
            temp = self.head
            self.head = self.head.next
            self.head.prev = None
            temp.next = None
            self.nodes -= 1
            return temp
    
    def deleteMid(self,pos):
        if self.head is None:
            return None
        else:
            if pos == 1:
                self.deleteStart()
            elif pos >= self.nodes:
                self.deleteEnd()
            else:
                curr, temp = self.head, self.head.next
                for _ in range(pos-2):
                    curr, temp = curr.next, temp.next
                curr.next = temp.next
                temp.next.prev = curr
                temp.prev = None
                temp.next = None
                self.nodes -= 1
                return temp
    
    def deleteEnd(self):
        if self.head is None:
            return None
        else:
            temp = self.tail
            self.tail = self.tail.prev
            temp.prev = None
            self.tail.next = None
            self.nodes -= 1
            return temp
    
    def display(self):
        if self.head is None:
            print('Empty Doubly Linked List')
        else:
            temp = self.head
            while temp is not None:
                print(temp.data, end='<-->')
                temp = temp.next
            print()
    
    def reverseDisplay(self):
        if self.head is None:
            print('Empty Doubly Linked List')
        else:
            temp = self.tail
            while temp is not None:
                print(temp.data, end='<-->')
                temp = temp.prev
            print()
