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
    int nodes;
	public:
    	Linkedlist() {
			head = NULL;
			tail = NULL;
			nodes = 0;
		}
    	void insertNode(int data) {
    		Node* newNode = new Node(data);
    		if (head == NULL) {
        		head = newNode;
        		tail = newNode;
        		nodes += 1;
        		return;
    		}
    		else {
    			nodes += 1;
				Node* temp = head;
    			for (int i=0; i<nodes-2; i++) {
        			temp = temp->next;
    			}
    			temp->next = newNode;
    			tail = newNode;
    			newNode->next = head;
    		}
		}
    	void printList() {
    		Node* temp = head;
    		if (head == NULL) {
        		cout << "List empty" << endl;
        		return;
    		}
    		for (int i=0; i<nodes; i++) {
        		cout << temp->data << "-->";
        		temp = temp->next;
    		}
    		cout<<endl;
		}
    	void deleteNode(int nodeOffset) {
    		Node *temp1 = head, *temp2 = head->next;
    		for (int i=1; i<nodeOffset-1; i++) {
    			temp1 = temp1->next;
    			temp2 = temp2->next;
			}
			temp1->next = temp2->next;
    		nodes -= 1;
		}
};
int main() {
    Linkedlist list;
    int n,val;
    cout << "Enter the Number of Elements: ";
    cin>>n;
    int arr[n];
    for (int i=0; i<n; i++){
    	cout << "Enter the Element: ";
    	cin>>val;
    	list.insertNode(val);
	}
    cout << "Elements of the list are: ";
    list.printList();
    cout << endl;
    cout<<"Enter the index to element to delete: ";
    cin>>val;
    list.deleteNode(val);
    cout << "Elements of the list are: ";
    list.printList();
    cout << endl;
    return 0;
}
