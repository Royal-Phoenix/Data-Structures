import java.util.*;
class Array {
    private int arr[];
    private int count;
    Array() {
        arr = new int[100];
        count = 0;
    }
    public void Append(int val) {
        arr[count] = val;
        count++;
    }
    public void Create() {
        Scanner t = new Scanner(System.in);
        int n, val;
        System.out.print("Enter the Number of Elements : ");
        n = t.nextInt();
        for (int i=0; i<n; i++) {
            System.out.print("Enter the Element : ");
            val = t.nextInt();
            Append(val);
        }
    }
    public void Search(int key) {
        for (int i=0; i<count; i++) {
            if (arr[i] == key) {
                System.out.print("Element found at Index " + i);
            }
        }
    }
    public void Display() {
        System.out.print("Array Elements : ");
        for (int i=0; i<count; i++) {
            System.out.print(arr[i] + " ");
        }
        System.out.print(" ");
    }
    public void Sort() {
        int temp, min_ind;
        for (int i=0; i<count; i++) {
            min_ind = i;
            for(int j=0; j<count; j++) {
                if (arr[j] < arr[min_ind]) {
                    temp = arr[j];
                    arr[j] = arr[min_ind];
                    arr[min_ind] = temp;
                }
            }
        }
    }
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        int val;
        Array obj = new Array();
        obj.Create();
        obj.Display();
        System.out.print("\nEnter a Element to Append : ");
        val = s.nextInt();
        obj.Append(val);
        obj.Display();
        System.out.print("\nEnter the Search Element : ");
        val = s.nextInt();
        obj.Search(val);
        System.out.print("\nSorting Array Elements\n");
        obj.Sort();
        obj.Display();
    }
}