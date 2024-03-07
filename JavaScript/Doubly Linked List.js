class Node {
    constructor(data) {
        this.data = data;
        this.prev = null;
        this.next = null;
    }
}

class DoublyLinkedList {
    constructor() {
        this.head = null;
        this.tail = null;
        this.nodes = 0;
    }
    insertStart(data) {
        const newNode = new Node(data);
        if (this.head == null) {
            this.head = newNode;
            this.tail = newNode;
        }
        else {
            newNode.next = this.head;
            this.head.prev = newNode;
            this.head = newNode;
        }
        this.nodes += 1;
    }
    insertMid(pos, data) {
        if (this.head == null) {
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
                let curr = this.head, temp = this.head.next;
                for (let i=0; i<pos-2; i++) {
                    curr = curr.next;
                    temp = temp.next;
                }
                curr.next = newNode;
                newNode.prev = curr;
                newNode.next = temp;
                temp.prev = newNode;
                this.nodes += 1;
            }
        }
    }
    insertEnd(data) {
        const newNode = new Node(data);
        if (this.head == null) {
            this.head = newNode;
            this.tail = newNode;
        }
        else {
            this.tail.next = newNode;
            newNode.prev = this.tail;
            this.tail = newNode;
        }
        this.nodes += 1;
    }
    deleteStart() {
        if (this.head == null)
            console.log('Empty Linked List');
        else {
            const temp = this.head;
            this.head = this.head.next;
            this.head.prev = null;
            temp.next = null;
            this.nodes -= 1;
        }
    }
    deleteMid(pos) {
        if (this.head == null)
            console.log('Empty Linked List');
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
                temp.next.prev = curr;
                temp.next = null;
                temp.prev = null;
                this.nodes -= 1;
            }
        }
    }
    deleteEnd() {
        if (this.head == null)
            console.log('Empty Linked List');
        else {
            const temp = this.tail;
            this.tail = this.tail.prev;
            temp.prev = null;
            this.tail.next = null;
            this.nodes -= 1;
        }
    }
    display() {
        if (this.head === null)
            console.log('Emppty Doubly Linked List');
        else {
            let temp = this.head;
            let data = ``;
            for (let i=0; i<this.nodes; i++) {
                data += `${temp.data}<-->`
                temp = temp.next;
            }
        }
        console.log(data);
    }
    reverseDisplay() {
        let temp = this.tail;
        let data = ``;
        for (let i=0; i<this.nodes; i++) {
            data += `${temp.data}<-->`
            temp = temp.prev;
        }
        console.log(data);
    }
}
