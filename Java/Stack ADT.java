import java.util.*;
class Stack {
    private int stack[];
    private int top;
    private int capacity;
    Stack(int size) {
        stack = new int[size];
        capacity = size;
        top = -1;
    }
    public Boolean isEmpty() {
        return top == -1;
    }
    public Boolean isFull() {
        return top == capacity - 1;
    }

    public void push(int value) {
        if (isFull()) {
            System.out.println("STACK FULL");
            System.exit(1);
        }
        stack[++top] = value;
    }
    public int pop() {
        if (isEmpty()) {
            System.out.println("STACK EMPTY");
            System.exit(1);
        }
        return stack[top--];
    }
    public void display() {
        System.out.print("  STACK\n");
        for (int i = top; i > -1; i--) {
            System.out.print("|       |\n");
            System.out.print("|   " + stack[i] + "   |\n");
            System.out.print("|_______|\n");
        }
    }
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        int n,val;
        System.out.print("Enter the Number of Elements : ");
        n = s.nextInt();
        Stack obj = new Stack(n);
        for (int i=0; i<n; i++) {
            System.out.print("Enter the Element : ");
            val = s.nextInt();
            obj.push(val);
        }
        obj.display();
        System.out.print("\nPopping Stack Element\n\n");
        obj.pop();
        obj.display();
    }
}