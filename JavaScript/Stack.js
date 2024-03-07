class Node {
    constructor(data) {
        this.data = data;
        this.next = null;
    }
}

class Stack {
    constructor() {
        this.top = null;
        this.bottom = null;
        this.nodes = 0;
    }
    pushValue(data) {
        const newNode = new Node(data);
        if (this.bottom === null) {
            this.top = newNode;
            this.bottom = newNode;
        }
        else {
            newNode.next = this.top;
            this.top = newNode;
        }
        this.nodes += 1;
    }
    popValue() {
        if (this.bottom === null)
            return 'Empty Stack';
        else {
            const temp = this.top;
            this.top = this.top.next;
            temp.next = null;
            this.nodes -= 1;
            return temp;
        }
    }
    peekValue() {
        return this.top;
    }
    searchValue(data) {
        let temp = this.top, pos = 1;
        while (temp !== null) {
            if (temp.data == data) {break;}
            temp = temp.next;
            pos += 1;
        }
        if (pos > this.nodes) {return null;}
        else {return pos;}
    }
    display() {
        if (this.bottom === null)
            console.log('Empty Stack');
        else {
            let temp = this.top, data = ``;
            while (temp !== null) {
                data += `${temp.data} `;
                temp = temp.next;
            }
            console.log(data);
        }
    }
}
