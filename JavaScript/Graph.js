class Graph {
    constructor() {
        this.graph = {};
        this.vertices = 0;
    }
    addEdge(src, dest, isBidirectional=false) {
        if (this.graph[src] === undefined)
            this.graph[src] = [];
        if (this.graph[dest] === undefined)
            this.graph[dest] = [];
        if (this.graph[src] !== undefined && this.graph[dest] !== undefined)
            this.graph[src].push(dest);
            if (isBidirectional === true)
                this.graph[dest].push(src)
    }
}
