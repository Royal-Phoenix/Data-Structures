class Node:
    def __init__(self,data):
        self.data, self.left, self.right = data, None, None

class BinarysearchNodeTree:
    def __init__(self):
        self.root, self.nodes = None, 0
    
    def insertNode(self, root, data):
        if root is not None:
            if data <= root.data:
                root.left = self.insertNode(root.left, data)
            else:
                root.right = self.insertNode(root.right, data)
        else:
            self.nodes += 1
            return Node(data)
        return root
    
    def searchNode(self, root, data, path='', flag=False):
        if root is None or root.data == data:
            return path if root is not None else None
        elif data <= root.data:
            return self.searchNode(root.left, data, path+'0', flag)
        else:
            return self.searchNode(root.right, data, path+'1', flag)
    
    def deleteNode(self, root, data):
        if root is None:
            return root
        if root.data > data:
            root.left = self.deleteNode(root.left, data)
            return root
        elif root.data < data:
            root.right = self.deleteNode(root.right, data)
            return root
        if root.left is None:
            temp = root.right
            del root
            return temp
        elif root.right is None:
            temp = root.left
            del root
            return temp
        else:
            succParent = root
            succ = root.right
            while succ.left is not None:
                succParent = succ
                succ = succ.left
            if succParent != root:
                succParent.left = succ.right
            else:
                succParent.right = succ.right
            root.data = succ.data
            del succ
            return root
    
    def inOrder(self, root):
        if root is not None:
            self.inOrder(root.left)
            print(root.data, end='-->')
            self.inOrder(root.right)
    
    def preOrder(self, root):
        if root is not None:
            print(root.data, end='-->')
            self.preOrder(root.left)
            self.preOrder(root.right)
    
    def postOrder(self, root):
        if root is not None:
            self.postOrder(root.left)
            self.postOrder(root.right)
            print(root.data, end='-->')
