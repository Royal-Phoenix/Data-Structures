class Node:
    def __init__(self, data):
        self.data, self.next = data, None

class Queue:
    def __init__(self):
        self.front, self.rear, self.nodes = None, None, 0
    
    def enqueueValue(self, data):
        new = Node(data)
        if self.front is None:
            self.front, self.rear = new, new
        else:
            self.rear.next = new
            self.rear = new
        self.nodes += 1
    
    def dequeueValue(self):
        if self.front is None:
            return None
        else:
            temp = self.front
            self.front = self.front.next
            temp.next = None
            self.nodes += 1
            return temp
    
    def peekValue(self):
        return self.front
    
    def searchValue(self, data):
        temp, pos = self.front, 1
        for _ in range(self.nodes):
            if temp.data == data:
                break
            temp = temp.next
            pos += 1
        return None if pos > self.nodes else pos
    
    def display(self):
        if self.front is None:
            print('Empty Queue')
        else:
            temp = self.front
            while temp is not None:
                print(temp.data, end=' ')
                temp = temp.next
            print()
