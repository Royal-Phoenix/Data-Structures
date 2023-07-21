#include<iostream>
using namespace std;
void Bubble_Sort(int arr[], int size) {
	int temp;
	for (int i=0; i<(size-1); i++) {
		for (int j=0; j<(size-1); j++) {
			if (arr[j] > arr[j+1]) {
				temp = arr[j];
				arr[j] = arr[j+1];
				arr[j+1] = temp;
			}
		}
	}
	cout<<"\nSorted Array by Bubble Sort :";
}
void Selection_Sort(int arr[], int size) {
	int temp,min_ind;
	for (int i=0; i<(size-1); i++) {
		min_ind = i;
		for (int j=i+1; j<size; j++) {
			if (arr[j] < arr[min_ind]) {
				temp = arr[j];
				arr[j] = arr[min_ind];
				arr[min_ind] = temp;
			}
		}
	}
	cout<<"\nSorted Array by Selection Sort :";
}
void Insertion_Sort(int arr[], int size) {
	int temp,pos;
	for (int i=1; i<size; i++) {
		temp = arr[i];
		pos = i-1;
		while (temp < arr[pos] && pos >= 0) {
			arr[pos+1] = arr[pos];
			pos -= 1;
		}
		arr[pos+1] = temp;
	}
	cout<<"\nSorted Array by Insertion Sort :";
}
int main() {
	int n,choice;
	cout<<"Enter the Number of Elements : ";
	cin>>n;
	int arr[n];
	for (int i=0; i<n; i++) {
		cout<<"Enter the Element : ";
		cin>>arr[i];
	}
	cout<<"\n\nMENU\n1.Bubble Sort\n2.Selection Sort\n3.Insertion Sort\n";
	cout<<"\nEnter the Choice : ";
	cin>>choice;
	switch(choice) {
		case 1:
			Bubble_Sort(arr,n);
			break;
		case 2:
			Selection_Sort(arr,n);
			break;
		case 3:
			Insertion_Sort(arr,n);
			break;
		default:
			cout<<"Invalid Choice \1\1\1";
	}
	if (choice >= 1 && choice <= 3) {
		for (int k=0; k<n; k++) {
			cout<<arr[k]<<" ";
		}
	}
	return 0;
}
