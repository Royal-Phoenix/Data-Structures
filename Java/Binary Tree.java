import java.util.*;
class BinaryTree {
    BinaryTree left;
    int data;
    BinaryTree right;
    BinaryTree(int value) {
        left = null;
        data = value;
        right = null;
    }
    public BinaryTree insert(BinaryTree root, int value) {
        if (root == null) {
            return new BinaryTree(value);
        }
        if (value > root.data) {
	        root.right = insert(root.right, value);
        }
        else if (value < root.data) {
	        root.left = insert(root.left, value);
        }
        return root;
    }
    public void inOrder(BinaryTree root) {
        if (root != null) {
            inOrder(root.left);
            System.out.print(" " + root.data);
            inOrder(root.right);
        }
    }
    public void preOrder(BinaryTree root) {
        if (root != null) {
            System.out.print(" " + root.data);
            preOrder(root.left);
            preOrder(root.right);
        }
    }
    public void postOrder(BinaryTree root) {
        if (root != null) {
            postOrder(root.left);
            postOrder(root.right);
            System.out.print(" " + root.data);
        }
    }
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        BinaryTree obj;
        int n, value;
        System.out.print("Enter the Number of Elements : ");
        n = s.nextInt();
        System.out.print("Enter the Root Value : ");
        value = s.nextInt();
        obj = new BinaryTree(value);
        for (int i=0; i<n-1; i++) {
    	    System.out.print("Enter the Element : ");
    	    value = s.nextInt();
    	    obj.insert(obj, value);
	    }
        System.out.print("\n\nDisplaying Binary Tree Elements in Inorder\n");
        obj.inOrder(obj);
        System.out.print("\n\nDisplaying Binary Tree Elements in Preorder\n");
        obj.preOrder(obj);
        System.out.print("\n\nDisplaying Binary Tree Elements in Postorder\n");
        obj.postOrder(obj);
    }
}