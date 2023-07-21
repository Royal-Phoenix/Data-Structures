#include <iostream>
#include <string.h>
using namespace std;
#define SIZE 50
class Queue {
	private:
  		int queue[SIZE], front, rear, size;
	public:
  		Queue() {
    		front = -1;
    		rear = -1;
    		size = 0;
  		}
  		bool isFull() {
    		return front == 0 && rear == SIZE - 1;
  		}
  		bool isEmpty() {
    		return front == -1;
  		}
  		void enQueue(int value) {
    		if (isFull()) {
      			cout << "QUEUE FULL";
    		}
			else {
      			if (front == -1)
					front = 0;
      			queue[++rear] = value;
    		}
    		size++;
  		}
  		int deQueue() {
    		if (isEmpty()) {
      			cout << "QUEUE EMPTY" << endl;
      			return (-1);
    		}
			else {
      			if (front >= rear) {
        			front = -1;
        			rear = -1;
      			}
      			size--;
      			return queue[front++];
    		}
  		}
		void display() {
			string a="______",b="|     ",c="|_____";
			for (int i=0; i<size-1; i++) {
				a += "______"; b += "|     "; c += "|_____";
			}
			cout << "   QUEUE\n" << a << "\n" << b <<endl;
      		for (int i = front; i <= rear; i++)
        		cout << "|  " << queue[i] << "  ";
        	cout << "\n" << c << endl << endl;
    	}
};
int main() {
	Queue obj;
	int n, val;
	cout << "Enter the Number of Elements : ";
	cin>>n;
	for (int i=0; i<n; i++) {
        cout << "Enter the Element : ";
        cin>>val;
        obj.enQueue(val);
    }
  	obj.display();
  	cout << "\nDequeuing Queue Element\n\n";
    obj.deQueue();
    obj.display();
  	return 0;
}
