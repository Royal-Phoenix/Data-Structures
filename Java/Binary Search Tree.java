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
    public Boolean search(BinaryTree root, int value) {
        if (root.data == value) {
            return true;
        }
        if (value > root.data) {
	        return search(root.right, value);
        }
        else if (value < root.data) {
	        return search(root.left, value);
        }
        return false;
    }
    public void inOrder(BinaryTree root) {
        if (root != null) {
            inOrder(root.left);
            System.out.print(" " + root.data);
            inOrder(root.right);
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
        System.out.print("\n\nDisplaying BST Elements in Inorder\n");
        obj.inOrder(obj);
        System.out.print("\n\nEnter the Search Node : ");
        value = s.nextInt();
        if (obj.search(obj, value)) {
    	    System.out.print(value + "is Found");
	    }
	    else {
		    System.out.print(value + " is not Found");
	    }
    }
}