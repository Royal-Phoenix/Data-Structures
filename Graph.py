class Node:
    def __init__(self, data, coords):
        self.data = data
        self.X, self.Y, self.Z = coords
        self.neighbours = {}

class Graph:
    def __init__(self):
        self.graph, self.vertices = {}, 0
    def addVertex(self, vertex, coords):
        if vertex not in self.graph:
            self.graph[vertex] = Node(vertex, coords)
    def addEdge(self, src, dest, isBidirectional=False):
        if src in self.graph and dest in self.graph:
            self.graph[src].neighbours[dest] = self.graph[dest]
            if isBidirectional is True:
                self.graph[dest].neighbours[src] = self.graph[src]

obj = Graph()
obj.addVertex('Home', [0, 0, 0])
obj.addVertex('Beach', [1, 1, 0])
obj.addVertex('Theatre', [0, 0, 1])
obj.addVertex('Restaurant', [1, 1, 1])
obj.addEdge('Home', 'Theatre', True)
obj.addEdge('Home', 'Restaurant', True)
obj.addEdge('Restaurant', 'Beach')
obj.addEdge('Beach', 'Theatre')
for i in obj.graph:
    print(obj.graph[i].data, obj.graph[i].X, obj.graph[i].Y, obj.graph[i].Z, end='-->')
    for j in obj.graph[i].neighbours:
        print(obj.graph[j].data, obj.graph[j].X, obj.graph[j].Y, obj.graph[j].Z, end='||')
    print()
