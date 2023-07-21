#include<iostream>
using namespace std;
void Merge(int arr[], int p, int q, int r) {
	int n1 = q - p + 1;
  	int n2 = r - q;
	int L[n1], M[n2];
  	for (int i = 0; i < n1; i++)
    	L[i] = arr[p + i];
  	for (int j = 0; j < n2; j++)
    	M[j] = arr[q + 1 + j];
  	int i, j, k;
  	i = 0;
  	j = 0;
  	k = p;
  	while (i < n1 && j < n2) {
    	if (L[i] <= M[j]) {
      		arr[k] = L[i];
      		i++;
    	}
		else {
      		arr[k] = M[j];
      		j++;
    	}
    	k++;
  	}
  	while (i < n1) {
    	arr[k] = L[i];
    	i++;
    	k++;
  	}
  	while (j < n2) {
    	arr[k] = M[j];
    	j++;
    	k++;
  	}
}
void Merge_Sort(int arr[], int l, int r) {
  	if (l < r) {
    	int m = l + (r - l) / 2;
    	Merge_Sort(arr, l, m);
    	Merge_Sort(arr, m + 1, r);
    	Merge(arr, l, m, r);
  	}
}
void Swap(int *a, int *b) {
	int t = *a;
	*a = *b;
	*b = t;
}
int Partition(int array[], int low, int high) {
	int pivot = array[high];
  	int i = low - 1;
  	for (int j = low; j < high; j++) {
    	if (array[j] <= pivot) {
      		i++;
      		Swap(&array[i], &array[j]);
    	}
  	}
  	Swap(&array[i + 1], &array[high]);
  	return (i + 1);
}
void Quick_Sort(int array[], int low, int high) {
  	if (low < high) {
    	int pi = Partition(array, low, high);
    	Quick_Sort(array, low, pi - 1);
    	Quick_Sort(array, pi + 1, high);
  	}
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
	cout<<"\n\nMENU\n1.Merge Sort\n2.Quick Sort\n";
	cout<<"\nEnter the Choice : ";
	cin>>choice;
	switch(choice) {
		case 1:
			Merge_Sort(arr, 0, n-1);
			cout<<"Sorted Array by Merge Sort : ";
			break;
		case 2:
			Quick_Sort(arr, 0, n-1);
			cout<<"Sorted Array by Quick Sort : ";
			break;
		default:
			cout<<"Invalid Choice \1\1\1";
	}
	if (choice == 1 || choice == 2) {
		for (int k=0; k<n; k++) {
			cout<<arr[k]<<" ";
		}
	}
	return 0;
}
