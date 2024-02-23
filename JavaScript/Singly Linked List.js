class Node {
    constructor(data) {
        this.data = data;
        this.next = data;
    }
}

class LinkedList {
    constructor() {
        this.head = null;
        this.tail = null;
    }
    insert(data) {
        let newNode = new Node(data)
        if (this.head == null) {
            this.head = newNode;
            this.tail = newNode;
        }
        else {
            this.tail.next = newNode;
            this.tail = newNode;
        }
    }
    display() {
        let temp = this.head;
        while (temp !== null) {
            console.log(temp.data);
            temp = temp.next;
        }
    }
}

var obj = new LinkedList();
obj.insert(10);
obj.insert(20);
obj.insert(30);
function func() {
    obj.display()
}
