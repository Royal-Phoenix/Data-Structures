class Graph:
    def __init__(self):
        self.graph = {}
        self.vertices = 0
    
    def add_vertex(self,v):
        if v in self.graph:
            print("Vertex ", v, " already exists.")
        else:
            self.vertices += 1
            self.graph[v] = []
    
    def add_edge(self,v1,v2):
        if v1 not in self.graph:
            print("Vertex ", v1, " does not exist.")
        elif v2 not in self.graph:
            print("Vertex ", v2, " does not exist.")
        else:
            self.graph[v1].append(v2)
        
    def print_graph(self):
        for vertex in self.graph:
            for edges in self.graph[vertex]:
                print(vertex, " -> ", edges)
        print("Internal representation")
        for i in self.graph:
            print(i,":",self.graph[i])

    def DFS_Util(self,v,visited):
        visited.add(v)
        print(v," ",end = "")
        for i in self.graph[v]:
            if i not in visited:
                self.DFS_Util(i,visited)
    
    def DFS(self,v):
        visited = set()
        self.DFS_Util(v,visited)
        print()
    
    def DFS1(self,node,visited):
        if node not in visited:
            visited.add(node)
            print(node,"",end = " ")
            for i in self.graph[node]:
                self.DFS1(i,visited)
    
    def BFS(self,v):
        visited = [False]*(max(self.graph) + 1)
        queue = []
        queue.append(v)
        visited[v] = True
        while queue:
            v = queue.pop()
            print(v," ",end = "")
            for i in self.graph[v]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True
        print()

    def Sort_Util(self,n,visited,stack):
        visited[n] = True
        for element in self.graph[n]:
            if visited[element] == False:
                self.Sort_Util(element,visited,stack)
        stack.insert(0,n)

    def TopologicalSort(self):
        visited = [False]*self.vertices
        stack = []
        for element in range(self.vertices):
            if visited[element] == False:
                self.Sort_Util(element,visited,stack)
        print(stack)
    
obj = Graph()
obj.add_vertex(1)
obj.add_vertex(2)
obj.add_vertex(3)
obj.add_vertex(4)
obj.add_edge(1, 2)
obj.add_edge(1, 3)
obj.add_edge(2, 3)
obj.add_edge(3, 1)
obj.add_edge(3, 4)
obj.add_edge(4, 4)
visited = set()
obj.print_graph()
print("Depth First Search from Vertex 2")
obj.DFS(2)
print("Breadth First Search from Vertex 3")
obj.BFS(3)
