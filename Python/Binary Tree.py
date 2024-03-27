class Node:
    def __init__(self,data):
        self.data, self.left, self.right = data, None, None

class BinaryTree:
    def __init__(self):
        self.root, self.nodes = None, 0
    
    def insertNode(self, data):
        self.nodes += 1
        if self.root is not None:
            path, root = bin(self.nodes)[3:], self.root
            for direction in path[:-1]:
                root = root.left if direction == '0' else root.right
            if path[-1] == '0':
                root.left = Node(data)
            else:
                root.right = Node(data)
        else:
            self.root = Node(data)
    
    def deleteNode(self):
        if self.nodes > 1:
            path, root = bin(self.nodes)[3:], self.root
            for direction in path[:-1]:
                root = root.left if direction == '0' else root.right
            if path[-1] == '0':
                root.left = None
            else:
                root.right = None
        else:
            self.root = None
        self.nodes -= 1
    
    def searchNode(self, data):
        queue, count = [self.root], 1
        while queue is not None:
            root, queue = queue[0], queue[1:]
            if root.data == data:
                return count
            if root.left is not None:
                queue.append(root.left)
                count += 1
            if root.right is not None:
                queue.append(root.right)
                count += 1
    
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
