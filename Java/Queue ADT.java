import java.util.*;
class Queue {
    int queue[];
    int front, rear;
    int capacity,size;
    Queue(int length) {
        queue = new int[length];
        capacity = length;
        size = 0;
        front = -1;
        rear = -1;
    }
    public boolean isFull() {
        return front == 0 && rear == capacity - 1;
    }
    public boolean isEmpty() {
        return front == -1;
    }
    public void enQueue(int value) {
        if (isFull()) {
            System.out.println("QUEUE FULL");
            System.exit(1);
        }
        else {
            if (front == -1)
                front = 0;
            queue[++rear] = value;
        }
        size++;
    }
    public int deQueue() {
        if (isEmpty()) {
            System.out.println("QUEUE EMPTY");
            return -1;
        }
        else {
            if (front >= rear) {
                front = -1;
                rear = -1;
            }
            size--;
            return queue[front++];
        }
    }
    public void display() {
        String a, b, c;
        for (int i=0; i<size-1; i++) {
            a += "______"; b += "|     "; c += "|_____";
        }
        System.out.print("   QUEUE\n" + a + "\n" + b + "\n");
        for (int i = front; i <= rear; i++)
            System.out.print("|  " + queue[i] + "  ");
        System.out.print("\n");
        System.out.print(c + "\n");
    }
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        int n,val;
        System.out.print("Enter the Number of Elements : ");
        n = s.nextInt();
        Queue obj = new Queue(n);
        for (int i=0; i<n; i++) {
            System.out.print("Enter the Element : ");
            val = s.nextInt();
            obj.enQueue(val);
        }
        obj.display();
        System.out.print("\nDequeuing Queue Element\n\n");
        obj.deQueue();
        obj.display();
    }
}