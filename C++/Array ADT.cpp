#include<iostream>
using namespace std;
#define N 100
class Array {
	int arr[N];
	int count;
	public:
		Array() {
			count = 0;
		}
		void Append(int val) {
			arr[count] = val;
			count += 1;
		}
		void Create() {
			int n,val;
			cout << "Enter the Number of Elements : ";
			cin>>n;
			for (int i=0; i<n; i++) {
				cout << "Enter the Element : ";
				cin>>val;
				Append(val);
			}
		}
		void Search(int key) {
			for (int i=0; i<count; i++) {
				if (arr[i] == key) {
					cout << "Element found at Index " << i << endl;
				}
			}
		}
		void Display() {
			cout << "Array Elements : ";
			for (int i=0; i<count; i++) {
				cout << arr[i] << " ";
			}
			cout << endl;
		}
		void Sort() {
			int temp,min_ind;
			for (int i=0; i<(count-1); i++) {
				min_ind = i;
				for (int j=i+1; j<count; j++) {
					if (arr[j] < arr[min_ind]) {
						temp = arr[j];
						arr[j] = arr[min_ind];
						arr[min_ind] = temp;
					}
				}
			}
		}
};
int main() {
	int val;
	Array obj;
	obj.Create();
	obj.Display();
	cout << "Enter a Element to Append : ";
	cin>>val;
	obj.Append(val);
	obj.Display();
	cout << "Enter the Search Element : ";
	cin>>val;
	obj.Search(val);
	cout << "Sorting Array Elements" << endl;
	obj.Sort();
	obj.Display();
}
