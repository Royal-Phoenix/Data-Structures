#include <iostream>
#include <stdlib.h>
using namespace std;
#define SIZE 50
class Stack {
	private:
		int stack[SIZE],top;
	public:
		Stack() {
			int stack[SIZE];
			top = -1;
		}
		bool isEmpty() {
			return top == -1;
		}
		bool isFull() {
			return top == SIZE - 1;
		}
		void push(int value) {
			if (isFull()) {
				cout << "STACK FULL" << endl;
			}
			stack[++top] = value;
		}
		int pop() {
			if ((isEmpty())) {
				cout << "STACK EMPTY" << endl;
			}
			return stack[top--];
		}
		void display() {
			cout << "  STACK" << endl;
			for (int i=top; i>-1; i--) {
				cout << "|       |" << endl;
				cout << "|   " << stack[i] << "   |" << endl;
				cout << "|_______|" << endl;
			}
			cout << endl;
		}
};
int main() {
	Stack obj;
	int n, val;
	cout << "Enter the Number of Elements : ";
	cin>>n;
	for (int i=0; i<n; i++) {
        cout << "Enter the Element : ";
        cin>>val;
        obj.push(val);
    }
  	obj.display();
  	cout << "Popping Stack Element\n\n";
    obj.pop();
    obj.display();
  	return 0;
}
