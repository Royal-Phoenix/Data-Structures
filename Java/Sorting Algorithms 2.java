import java.util.*;
class Sorts2 {
    static void Merge(int arr[], int p, int q, int r) {
    	int n1 = q - p + 1;
      	int n2 = r - q;
    	int L[], M[];
    	L = new int[n1];
    	M = new int[n2];
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
    static void Merge_Sort(int arr[], int l, int r) {
      	if (l < r) {
        	int m = l + (r - l) / 2;
        	Merge_Sort(arr, l, m);
        	Merge_Sort(arr, m + 1, r);
        	Merge(arr, l, m, r);
      	}
    }
    static int Partition(int array[], int low, int high) {
    	int pivot = array[high];
      	int i = low - 1;
      	for (int j = low; j < high; j++) {
        	if (array[j] <= pivot) {
          		i++;
          		int temp = array[i];
          		array[i] = array[j];
          		array[j] = temp;
        	}
      	}
      	int temp = array[i + 1];
        array[i + 1] = array[high];
        array[high] = temp;
      	return (i + 1);
    }
    static void Quick_Sort(int array[], int low, int high) {
      	if (low < high) {
        	int pi = Partition(array, low, high);
        	Quick_Sort(array, low, pi - 1);
        	Quick_Sort(array, pi + 1, high);
      	}
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
    	System.out.print("\n\nMENU\n1.Merge Sort\n2.Quick Sort\n");
    	System.out.print("\nEnter the Choice : ");
    	choice = s.nextInt();
    	switch(choice) {
    		case 1:
    			Merge_Sort(arr, 0, n-1);
    			System.out.print("Sorted Array by Merge Sort : ");
    			break;
    		case 2:
    			Quick_Sort(arr, 0, n-1);
    			System.out.print("Sorted Array by Quick Sort : ");
    			break;
    		default:
    			System.out.print("Invalid Choice \1\1\1");
    	}
		for (int k=0; k<n; k++) {
    		System.out.print(arr[k] + " ");
    	}
    }
}