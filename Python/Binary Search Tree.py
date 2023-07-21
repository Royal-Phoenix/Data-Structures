class Binary_Search_Tree:
    def __init__(self,data):
        self.root = data
        self.left = None
        self.right = None

    def Insert(self,data):
        if self.root is None:
            self.root = data
            return
        else:
            if self.root > data:
                if self.left:
                    self.left.Insert(data)
                else:
                    self.left = Binary_Search_Tree(data)
            elif self.root < data:
                if self.right:
                    self.right.Insert(data)
                else:
                    self.right = Binary_Search_Tree(data)
    
    def Search(self,data):
        if self.root == data:
            print("Element is Found")
            return
        else:
            if self.root > data:
                if self.left:
                    self.left.Search(data)
                else:
                    print("Element not Found")
            elif self.root < data:
                if self.right:
                    self.right.Search(data)
                else:
                    print("Element not Found")
                
    def Delete(self,data):
        if self.root is None:
            print("Tree is Empty")
            return
        else:
            if self.root > data:
                if self.left:
                    self.left = self.left.Delete(data)
                else:
                    print("Element not Found in Tree")
            elif self.root < data:
                if self.right:
                    self.right = self.right.Delete(data)
                else:
                    print("Element not Found in Tree")
            else:
                if self.left is None:
                    temp = self.right
                    self = None
                    return temp
                elif self.right is None:
                    temp = self.left
                    self = None
                    return temp
                node = self.right
                while node.left:
                    node = node.left
                self.root = node.root
                self.right = self.right.delete(node)       
    
    def InOrder(self):
        if self.left:
            self.left.InOrder()
        print(self.root," ",end = "")
        if self.right:
            self.right.InOrder()
    
    def PreOrder(self):
        print(self.root," ",end = "")
        if self.left:
            self.left.PreOrder()
        if self.right:
            self.right.PreOrder()
    
    def PostOrder(self):
        if self.left:
            self.left.PostOrder()
        if self.right:
            self.right.PostOrder()
        print(self.root," ",end = "")
    
    def Display(self):
        print()
        
obj = Binary_Search_Tree(int(input("Enter Root Node : ")))
arr = [20,4,30,1,5,6]
for i in arr:
    obj.Insert(i)
obj.Search(4)
obj.InOrder()
print()
obj.PreOrder()
print()
obj.PostOrder()
print()
