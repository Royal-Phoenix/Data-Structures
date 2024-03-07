class Node {
    constructor(data) {
        this.data = data;
        this.next = null;
    }
}

class CircularLinkedList {
    constructor() {
        this.head = null;
        this.tail = null;
        this.nodes = 0;
    }
    insertStart(data) {
        const newNode = new Node(data);
        if (this.head === null) {
            this.head = newNode;
            this.tail = newNode;
        }
        else {
            newNode.next = this.head;
            this.head = newNode;
            this.tail.next = this.head;
        }
        this.nodes += 1;
    }
    insertMid(pos, data) {
        if (this.head === null) {
            const newNode = new Node(data);
            this.head = newNode;
            this.tail = newNode;
            this.nodes += 1;
        }
        else {
            if (pos == 1)
                this.insertStart(data);
            else if (pos >= this.nodes)
                this.insertEnd(data);
            else {
                const newNode = new Node(data);
                let temp = this.head;
                for (let i=0; i<pos-2; i++)
                    temp = temp.next;
                newNode.next = temp.next;
                temp.next = newNode;
                this.nodes += 1;
            }
        }
    }
    insertEnd(data) {
        const newNode = new Node(data);
        if (this.head === null) {
            this.head = newNode;
            this.tail = newNode;
        }
        else {
            this.tail.next = newNode;
            this.tail = newNode;
            this.tail.next = this.head;
        }
        this.nodes += 1;
    }
    deleteStart() {
        if (this.head === null)
            console.log('Empty Circular Linked List');
        else {
            const temp = this.head;
            this.head = this.head.next;
            this.tail.next = this.head;
            temp.next = null;
            this.nodes -= 1;
        }
    }
    deleteMid(pos) {
        if (this.head === null)
            console.log('Empty Circular Linked List');
        else {
            if (pos == 1)
                this.deleteStart();
            else if (pos >= this.nodes)
                this.deleteEnd();
            else {
                let curr = this.head, temp = this.head.next;
                for (let i=0; i<pos-2; i++) {
                    curr = curr.next;
                    temp = temp.next;
                }
                curr.next = temp.next;
                temp.next = null;
                this.nodes -= 1;
            }
        }
    }
    deleteEnd() {
        if (this.head === null)
            console.log('Empty Circular Linked List');
        else {
            let temp = this.head;
            for (let i=0; i<this.nodes-2; i++) {
                temp = temp.next;
            }
            temp.next = this.head;
            this.tail.next = null;
            this.tail = temp;
            this.nodes -= 1;
        }
    }
    display() {
        if (this.head === null)
            console.log('Empty Circular Linked List');
        else {
            let temp = this.head, data = ``;
            for (let i=0; i<this.nodes; i++) {
                data += `${temp.data}->`
                temp = temp.next;
            }
            console.log(data);
        }
    }
}
