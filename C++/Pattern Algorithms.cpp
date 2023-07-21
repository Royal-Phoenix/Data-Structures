#include<iostream>
using namespace std;
void Pyramid(int n) {
	int k = 0;
	for (int i=1; i<=n; i++) {
		for (int j=1; j<((n-i)+1); j++) {
			cout<<" ";
		}
		while (k != ((2*i)-1)) {
			cout<<"*";
			k += 1;
		}
		k = 0;
		cout<<endl;
	}
}
void Level(int n) {
	int k = 0,i;
	for (i=1; i<=n; i++) {
		for (int j=1; j<((n-i)+1); j++) {
			cout<<" ";
		}
		while (k != ((2*i)-1)) {
			cout<<i;
			k += 1;
		}
		k = 0;
		cout<<endl;
	}
}
void Number(int n) {
	int k = 0;
	for (int i=1; i<=n; i++) {
		for (int j=1; j<((n-i)+1); j++) {
			cout<<" ";
		}
		while (k != ((2*i)-1)) {
			cout<<k+1;
			k += 1;
		}
		k = 0;
		cout<<endl;
	}
}
int main() {
	int n,k,j,choice;
	cout<<"\n\nMENU\n1.Pyramid Pattern";
	cout<<"\n2.Level Pattern\n3.Number Pattern\n\n";
	cout<<"Enter the Choice : ";
	cin>>choice;
	if (choice >= 1 && choice <= 3) {
		cout<<"Enter the Number of Rows : ";
		cin>>n;
	}
	switch(choice) {
		case 1:
			Pyramid(n);
			break;
		case 2:
			Level(n);
			break;
		case 3:
			Number(n);
			break;
		default:
			cout<<"Invalid Choice \1\1\1";
	}
	return 0;
}
