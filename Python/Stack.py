class Node:
    def __init__(self, data):
        self.data, self.next = data, None

class Stack:
    def __init__(self):
        self.top, self.bottom, self.nodes = None, None, 0
    
    def pushValue(self, data):
        new = Node(data)
        if self.bottom is None:
            self.top, self.bottom = new, new
        else:
            new.next = self.top
            self.top = new
        self.nodes += 1
    
    def popValue(self):
        if self.bottom is None:
            return None
        else:
            temp = self.top
            self.top = self.top.next
            temp.next = None
            self.nodes -= 1
            return temp
    
    def peekValue(self):
        return self.top
    
    def searchValue(self, data):
        temp, pos = self.top, 1
        while temp is not None:
            if temp.data == data:
                break
            temp = temp.next
            pos += 1
        return None if pos > self.nodes else pos
    
    def display(self):
        if self.bottom is None:
            print('Empty Stack')
        else:
            temp = self.top
            while temp is not None:
                print(temp.data, end=' ')
                temp = temp.next
            print()
