#include <bits/stdc++.h>
using namespace std;
class BST {
	public:
		BST *left;
		int data;
    	BST *right;
    	BST(int value) {
    		left = NULL;
    		data = value;
    		right = NULL;
		}
		BST* insert(BST* root, int value) {
			if (!root) {
		        return new BST(value);
		    }
		    if (value > root->data) {
		        root->right = insert(root->right, value);
		    }
		    else if (value < root->data) {
		        root->left = insert(root->left, value);
		    }
		    return root;
		}
		BST* search(BST* root, int value) {
			if (root == NULL || root->data == value) {
		        return root;
		    }
		    if (value > root->data) {
		        return search(root->right, value);
		    }
		    else if (value < root->data) {
		        return search(root->left, value);
		    }
		}
		void inOrder(BST* root) {
			if (!root) {
		        return;
		    }
		    inOrder(root->left);
		    cout << root->data << " ";
		    inOrder(root->right);
		}
};
int main() {
    BST *obj, *root = NULL;
    int n,value;
    cout << "Enter the Number of Elements : ";
    cin>>n;
    int arr[n];
    cout << "Enter the Root Value :";
    cin>>value;
    root = obj->insert(root, value);
    for (int i=0; i<n-1; i++) {
    	cout << "Enter the Element : ";
    	cin>>value;
    	obj->insert(root, value);
	}
    cout << "Displaying BST Elements in Inorder"<<endl;
    obj->inOrder(root);
    cout << "\nEnter the Search Node : ";
    cin>>value;
    if (obj->search(root, value)) {
    	cout << value << "is Found";
	}
	else {
		cout << value << " is not Found";
	}
    return 0;
}
