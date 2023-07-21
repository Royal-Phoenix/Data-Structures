#include<iostream>
using namespace std;
void Linear_Search(int arr[], int key, int size) {
    for (int i=0; i<size; i++) {
        if (arr[i] == key) {
            cout << key << " is found at index " <<i << " by Linear Search";
            break;
        }
    }
}
void Sentinel_Linear_Search(int arr[], int key, int size) {
    int end = arr[size - 1];
    arr[size - 1] = key;
    int i = 0;
    while (arr[i] != key) {
        i += 1;
    }
    arr[size - 1] = end;
    cout << key << " is found at index " << i << " by Sentinel Linear Search";
}
int Binary_Search(int arr[], int x, int y, int key) {
    int mid = (x + y) / 2;
    if (key < arr[mid]) {
        return Binary_Search(arr,x,mid-1,key);
    }
    else if (key > arr[mid]) {
        return Binary_Search(arr,mid+1,y,key);
    }
    else {
        return mid;
    }
}
int Ternary_Search(int arr[], int x, int y, int key) {
    int mid1,mid2;
    mid1 = x + ((y - 1) / 3);
    mid2 = y - ((y - 1) / 3);
    if (key < arr[mid1]) {
        return Ternary_Search(arr,x,mid1-1,key);
    }
    else if (key == arr[mid1]) {
        return mid1;
    }
    else if (key == arr[mid2]) {
        return mid2;
    }
    else if (key > arr[mid2]) {
        return Ternary_Search(arr,mid2+1,y,key);
    }
    else {
        return Ternary_Search(arr,mid1+1,mid2-1,key);
    }
}
int main() {
    int n,ind,key,choice;
    cout << "Enter the Number of Elements : ";
    cin>>n;
    int arr[n];
    for (int i=0; i<n; i++) {
        cout << "Enter the Element : ";
        cin>>arr[i];
    }
    cout << "Enter the search Element : ";
    cin>>key;
    cout << "\nMENU\n1.Linear Search\n2.Sentinel Linear Search";
    cout << "\n3.Binary Search\n4.Ternary Search\n\n";
    cout << "Enter the Choice : ";
    cin>>choice;
    switch(choice) {
        case 1:
            Linear_Search(arr, key, n);
            break;
    	case 2:
            Sentinel_Linear_Search(arr, key, n);
            break;
        case 3:
            ind = Binary_Search(arr, 0, n, key);
            cout << key << " is found at index " << ind << " by Binary Search";
            break;
        case 4:
            ind = Ternary_Search(arr, 0, n, key);
            cout << key << " is found at index " << ind << " by Ternary Search";
            break;
        default:
            cout << "Invalid Choice\1\1\1";
    }
    return 0;
}
