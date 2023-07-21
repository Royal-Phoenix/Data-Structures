class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []
    
    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])
    
    def find(self, parent, i):
        if parent[i] != i:
            parent[i] = self.find(parent, parent[i])
        return parent[i]

    def union(self, parent, rank, x, y):
        if rank[x] < rank[y]:
            parent[x] = y
        elif rank[x] > rank[y]:
            parent[y] = x
        else:
            parent[y] = x
            rank[x] += 1

    def KruskalMST(self):
        result = []
        i = 0
        e = 0
        self.graph = sorted(self.graph,key=lambda item: item[2])
        parent = []
        rank = []
        for node in range(self.V):
            parent.append(node)
            rank.append(0)
        while e < self.V - 1:
            u, v, w = self.graph[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)
            if x != y:
                e = e + 1
                result.append([u, v, w])
                self.union(parent, rank, x, y)
        minimumCost = 0
        print("Edges in the constructed MST\n")
        print(" Edges \t Weight")
        for u, v, weight in result:
            minimumCost += weight
            print(u,"---",v,"  ",weight)
        print("\nCost of Minimum Spanning Tree is", minimumCost)

obj = Graph(9)
obj.addEdge(0, 1, 4)
obj.addEdge(0, 7, 8)
obj.addEdge(1, 2, 8)
obj.addEdge(1, 7, 11)
obj.addEdge(2, 3, 7)
obj.addEdge(2, 5, 4)
obj.addEdge(2, 8, 2)
obj.addEdge(3, 4, 9)
obj.addEdge(3, 5, 14)
obj.addEdge(4, 5, 10)
obj.addEdge(5, 6, 2)
obj.addEdge(6, 7, 1)
obj.addEdge(6, 8, 6)
obj.addEdge(7, 8, 7)
obj.KruskalMST()

obj = Graph(4)
obj.addEdge(0, 1, 10)
obj.addEdge(0, 2, 6)
obj.addEdge(0, 3, 5)
obj.addEdge(1, 3, 15)
obj.addEdge(2, 3, 4) 
obj.KruskalMST()
