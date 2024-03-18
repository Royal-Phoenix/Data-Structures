class Node {
    constructor(data) {
        this.data = data;
        this.next = null;
    }
}

class Queue {
    constructor() {
        this.front = null;
        this.rear = null;
        this.nodes = 0;
    }
    enqueueValue(data) {
        const newNode = new Node(data);
        if (this.front === null) {
            this.front = newNode;
            this.rear = newNode;
        }
        else {
            this.rear.next = newNode;
            this.rear = newNode;
        }
        this.nodes += 1;
    }
    dequeueValue() {
        if (this.front === null)
            return null;
        else {
            const temp = this.front;
            this.front = this.front.next;
            temp.next = null;
            this.nodes -= 1;
            return temp;
        }
    }
    peekValue() {
        return this.front;
    }
    searchValue(data) {
        let temp = this.front, pos = 1;
        for (let i=0; i<this.nodes; i++) {
            if (temp.data == data) {break;}
            temp = temp.next;
            pos += 1;
        }
        if (pos > this.nodes) {return null;}
        else {return pos;}
    }
    display() {
        if (this.bottom === null)
            console.log('Empty Queue');
        else {
            let temp = this.front, data = ``;
            while (temp !== null) {
                data += `${temp.data} `;
                temp = temp.next;
            }
            console.log(data);
        }
    }
}
