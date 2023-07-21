import java.util.*;
class Search {
    public static void Linear_Search(int arr[], int key) {
        for (int i=0; i<arr.length; i++) {
            if (arr[i] == key) {
                System.out.println(key + " is found at index " + i + " by Linear Search");
                break;
            }
        }
    }
    public static void Sentinel_Linear_Search(int arr[], int key) {
        int end = arr[arr.length - 1];
        arr[arr.length - 1] = key;
        int i = 0;
        while (arr[i] != key) {
            i += 1;
        }
        arr[arr.length - 1] = end;
        System.out.println(key + " is found at index " + i + " by Sentinel Linear Search");
    }
    public static int Binary_Search(int arr[], int x, int y, int key) {
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
    public static int Ternary_Search(int arr[], int x, int y, int key) {
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
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        int n,arr[],ind,key,choice;
        System.out.print("Enter the Number of Elements : ");
        n = s.nextInt();
        arr = new int[n];
        for (int i=0; i<n; i++) {
            System.out.print("Enter the Element : ");
            arr[i] = s.nextInt();
        }
        System.out.print("Enter the search Element : ");
        key = s.nextInt();
        System.out.print("\nMENU\n1.Linear Search\n2.Sentinel Linear Search");
        System.out.print("\n3.Binary Search\n4.Ternary Search\n\n");
        System.out.print("Enter the Choice : ");
        choice = s.nextInt();
        switch(choice) {
            case 1:
                Linear_Search(arr, key);
                break;
            case 2:
                Sentinel_Linear_Search(arr, key);
                break;
            case 3:
                ind = Binary_Search(arr, 0, n, key);
                System.out.println(key + " is found at index " + ind + " by Binary Search");
                break;
            case 4:
                ind = Ternary_Search(arr, 0, n, key);
                System.out.println(key + " is found at index " + ind + " by Ternary Search");
                break;
            default:
                System.out.print("Invalid Choice\1\1\1");
        }
    }
}