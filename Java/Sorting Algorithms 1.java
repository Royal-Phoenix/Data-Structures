import java.util.*;
class Sorts1 {
    static void Bubble_Sort(int arr[], int size) {
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
    	System.out.print("\nSorted Array by Bubble Sort :");
    }
    static void Selection_Sort(int arr[], int size) {
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
    	System.out.print("\nSorted Array by Selection Sort :");
    }
    static void Insertion_Sort(int arr[], int size) {
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
    	System.out.print("\nSorted Array by Insertion Sort :");
    }
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
    	int arr[],n,choice;
    	System.out.print("Enter the Number of Elements : ");
    	n = s.nextInt();
    	arr = new int[n];
    	for (int i=0; i<n; i++) {
    		System.out.print("Enter the Element : ");
    		arr[i] = s.nextInt();
    	}
    	System.out.print("\n\nMENU\n1.Bubble Sort\n2.Selection Sort\n3.Insertion Sort\n");
    	System.out.print("\nEnter the Choice : ");
    	choice = s.nextInt();
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
    			System.out.print("Invalid Choice \1\1\1");
    	}
    	for (int k=0; k<n; k++) {
    		System.out.print(arr[k] + " ");
		}
    }
}