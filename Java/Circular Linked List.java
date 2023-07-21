import java.util.*;
public class LinkedList { 
    Node head;
    static int nodes;
    static class Node { 
        int data; 
        Node next; 
        Node(int d) { 
            data = d; 
            next = null; 
        } 
    }
    public static LinkedList insert(LinkedList list, int data) { 
        Node new_node = new Node(data); 
        if (list.head == null) { 
            list.head = new_node;
            list.nodes += 1;
        } 
        else {
            nodes += 1;
            Node temp = list.head; 
            for (int i=0; i<list.nodes-2; i++) { 
                temp = temp.next; 
            }
            temp.next = new_node;
            new_node.next = list.head;
        }
        return list; 
    }
    public static void delete(LinkedList list, int ind) {
        Node currNode = list.head;
        Node tempNode = list.head.next;
        for (int i=1; i<ind-1; i++) { 
            currNode = currNode.next;
            tempNode = tempNode.next;
        }
        currNode.next = tempNode.next;
        list.nodes -= 1;
    }
    public static void printList(LinkedList list) {
        Node currNode = list.head; 
        System.out.print("Circular LinkedList: ");
        for (int i=0; i<list.nodes; i++) { 
            System.out.print(currNode.data + " "); 
            currNode = currNode.next; 
        }
        System.out.println(" ");
    }
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        int n,val;
        LinkedList obj = new LinkedList();
        System.out.print("Enter the Number of Elements : ");
        n = s.nextInt();
        for (int i=0; i<n; i++) {
            System.out.print("Enter the Element : ");
            val = s.nextInt();
            obj = insert(obj, val);
        }
        printList(obj);
        System.out.print("Enter the Index of Element to delete : ");
        val = s.nextInt();
        obj.delete(obj, val);
        printList(obj);
    } 
}