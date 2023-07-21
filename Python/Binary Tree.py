class Binary_Tree:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
    
    def In_Order(self,root):
        if root:
            root.In_Order(root.left)
            print(str(root.data) + "-->",end = "")
            root.In_Order(root.right)
    
    def Pre_Order(self,root):
        if root:
            print(str(root.data) + "-->",end = "")
            root.Pre_Order(root.left)
            root.Pre_Order(root.right)
    
    def Post_Order(self,root):
        if root:
            root.Post_Order(root.left)
            root.Post_Order(root.right)
            print(str(root.data) + "-->",end = "")
            
a1 = Binary_Tree(35)
a2 = Binary_Tree(20)
a3 = Binary_Tree(40)
a4 = Binary_Tree(10)
a5 = Binary_Tree(5)
a6 = Binary_Tree(8)
a7 = Binary_Tree(50)
a1.left = a2
a1.right = a3
a2.left = a4 # a1.left.left = a4
a4.left = a5 # a1.left.right = a5
a5.right = a6 # a1.right.left = a6
a3.right = a7 # a1.right.right = a7
print("Inorder Traversal")
print(a1.In_Order(a1))
print("Preorder Traversal")
print(a1.Pre_Order(a1))
print("Postorder Traversal")
print(a1.Post_Order(a1))
