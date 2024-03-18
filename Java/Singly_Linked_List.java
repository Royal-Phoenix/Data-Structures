class Node {
    int data;
    Node next;
    public Node(int data) {
        this.data = data;
        this.next = null;
    }
}

class Singly_Linked_List {
    Node head, tail;
    int nodes;
    public Singly_Linked_List() {
        this.head = null;
        this.tail = null;
        this.nodes = 0;
    }
    public void insertStart(int data) {
        Node newNode = new Node(data);
        if (this.head == null) {
            this.head = newNode;
            this.tail = newNode;
        }
        else {
            newNode.next = this.head;
            this.head = newNode;
        }
        this.nodes += 1;
    }
    public void insertMid(int pos, int data) {
        if (this.head == null) {
            Node newNode = new Node(data);
            this.head = newNode;
            this.tail = newNode;
            this.nodes += 1;
        }
        else {
            if (pos == 1) {
                this.insertStart(data);
            }
            else if (pos >= this.nodes) {
                this.insertEnd(data);
            }
            else {
                Node newNode = new Node(data);
                Node curr = this.head, temp = this.head.next;
                for (int i=0; i<pos-2; i++) {
                    curr = curr.next;
                    temp = temp.next;
                }
                curr.next = newNode;
                newNode.next = temp;
                this.nodes += 1;
            }
        }
    }
    public void insertEnd(int data) {
        Node newNode = new Node(data);
        if (this.head == null) {
            this.head = newNode;
            this.tail = newNode;
        }
        else {
            this.tail.next = newNode;
            this.tail = newNode;
        }
        this.nodes += 1;
    }
    public Node deleteStart() {
        if (this.head == null)
            return null;
        else {
            Node temp = this.head;
            this.head = this.head.next;
            temp.next = null;
            this.nodes -= 1;
            return temp;
        }
    }
    public Node deleteMid(int pos) {
        if (this.head == null) {
            return null;
        }
        else {
            if (pos == 1) {
                return this.deleteStart();
            }
            else if (pos >= this.nodes) {
                return this.deleteEnd();
            }
            else {
                Node curr = this.head, temp = this.head.next;
                for (int i=0; i<pos-2; i++) {
                    curr = curr.next;
                    temp = temp.next;
                }
                curr.next = temp.next;
                temp.next = null;
                this.nodes -= 1;
                return temp;
            }
        }
    }
    public Node deleteEnd() {
        if (this.head == null)
            return null;
        else {
            Node curr = this.head;
            for (int i=0; i<this.nodes-2; i++) {
                curr = curr.next;
            }
            Node temp = curr.next;
            curr.next = null;
            this.tail = curr;
            this.nodes -= 1;
            return temp;
        }
    }
    public void display() {
        Node temp = this.head;
        while (temp != null) {
            System.out.print(temp.data + " ");
            temp = temp.next;
        }
        System.out.println();
    }
    public static void main(String[] args) {
        // Singly Linked List
    }
}
