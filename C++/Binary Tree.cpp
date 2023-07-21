#include <bits/stdc++.h>
using namespace std;
class BT {
	public:
		BT *left;
		int data;
    	BT *right;
    	BT(int value) {
    		left = NULL;
    		data = value;
    		right = NULL;
		}
		BT* insert(BT* root, int value) {
			if (!root) {
		        return new BT(value);
		    }
		    if (value > root->data) {
		        root->right = insert(root->right, value);
		    }
		    else if (value < root->data) {
		        root->left = insert(root->left, value);
		    }
		    return root;
		}
		BT* search(BT* root, int value) {
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
		void inOrder(BT* root) {
			if (!root) {
		        return;
		    }
		    inOrder(root->left);
		    cout << root->data << " ";
		    inOrder(root->right);
		}
		void preOrder(BT* root) {
			if (!root) {
		        return;
		    }
		    cout << root->data << " ";
		    preOrder(root->left);
		    preOrder(root->right);
		}
		void postOrder(BT* root) {
			if (!root) {
		        return;
		    }
		    postOrder(root->left);
		    postOrder(root->right);
		    cout << root->data << " ";
		}
};
int main() {
    BT *obj, *root = NULL;
    int n,value;
    cout << "Enter the Number of Elements : ";
    cin>>n;
    cout << "Enter the Root Value :";
    cin>>value;
    root = obj->insert(root, value);
    for (int i=0; i<n-1; i++) {
    	cout << "Enter the Element : ";
    	cin>>value;
    	obj->insert(root, value);
	}
    cout << "\nDisplaying Binary Tree Elements in Inorder"<<endl;
    obj->inOrder(root);
    cout << "\nDisplaying Binary Tree Elements in Preorder"<<endl;
    obj->preOrder(root);
    cout << "\nDisplaying Binary Tree Elements in Postorder"<<endl;
    obj->postOrder(root);
    return 0;
}
