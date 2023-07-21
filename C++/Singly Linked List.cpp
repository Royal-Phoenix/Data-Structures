#include <iostream>
using namespace std;
class Node {
	public:
    	int data;
    	Node* next;
    	Node(int data) {
        	this->data = data;
        	this->next = NULL;
    	}
};
class Linkedlist {
    Node* head;
    Node* tail;
	public:
    	Linkedlist() {
			head = NULL;
			tail = NULL;
		}
    	void insertNode(int data) {
    		Node* newNode = new Node(data);
    		if (head == NULL) {
        		head = newNode;
        		return;
    		}
    		else {
    			Node* temp = head;
    			while (temp->next != NULL) {
        			temp = temp->next;
    			}
    			temp->next = newNode;
    		}
		}
    	void printList() {
    		Node* temp = head;
    		if (head == NULL) {
        		cout << "List empty" << endl;
        		return;
    		}
    		while (temp != NULL) {
        		cout << temp->data << "-->";
        		temp = temp->next;
    		}
    		cout<<endl;
		}
    	void deleteNode(int nodeOffset) {
    		Node *temp1 = head, *temp2 = head->next;
    		for (int i=1; i<nodeOffset; i++) {
    			temp1 = temp1->next;
    			temp2 = temp2->next;
			}
			temp1->next = temp2->next;
		}
};
int main() {
    Linkedlist list;
    int n,val;
    cout << "Enter the Number of Elements: ";
    cin>>n;
    for (int i=0; i<n; i++){
    	cout << "Enter the Element: ";
    	cin>>val;
    	list.insertNode(val);
	}
    cout << "Elements of the list are: ";
    list.printList();
    cout << endl;
    cout<<"Enter the index of element to delete: ";
    cin>>val;
    list.deleteNode(val);
    cout << "Elements of the list are: ";
    list.printList();
    cout << endl;
    return 0;
}
