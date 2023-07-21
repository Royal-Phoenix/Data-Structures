import java.util.*;
public class LinkedList { 
    Node head;
    static int nodes;
    static class Node {
        Node prev;
        int data; 
        Node next; 
        Node(int d) {
            prev = null;
            data = d; 
            next = null; 
        } 
    }
    public static LinkedList insert(LinkedList list, int data) { 
        Node new_node = new Node(data); 
        if (list.head == null) {
            new_node.prev = null;
            list.head = new_node;
        } 
        else {
            Node temp = list.head; 
            while (temp.next != null) { 
                temp = temp.next; 
            }
            temp.next = new_node;
            new_node.prev = temp;
        }
        return list; 
    }
    public static void delete(LinkedList list, int ind) {
        Node currNode = list.head;
        Node tempNode = list.head.next;
        for (int i=1; i<ind; i++) { 
            currNode = currNode.next;
            tempNode = tempNode.next;
        }
        currNode.next = tempNode.next;
        tempNode.next.prev = currNode;
        tempNode.prev = null;
        tempNode.next = null;
    }
    public static void printList(LinkedList list) {
        Node currNode = list.head; 
        System.out.print("Doubly LinkedList: ");
        while (currNode != null) { 
            System.out.print("<-->" + currNode.data); 
            currNode = currNode.next; 
        }
        System.out.println("<-->");
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