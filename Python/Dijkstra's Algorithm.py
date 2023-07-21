class Graph:
    def __init__(self, vertices,graph):
        self.V = vertices
        self.graph = graph
    def printSolution(self, dist):
        print("Vertex \tDistance from Source")
        for node in range(self.V):
            print(node, "\t", dist[node])
    def minDistance(self, dist, sptSet):
         inf = 9999
         for u in range(self.V):
            if dist[u] < inf and sptSet[u] == False:
                inf = dist[u]
                min_index = u
         return min_index
    def dijkstra(self, src):
        dist = [9999] * self.V
        dist[src] = 0
        sptSet = [False] * self.V
        for v in range(self.V):
            x = self.minDistance(dist, sptSet)
            sptSet[x] = True
            for y in range(self.V):
                if self.graph[x][y] > 0 and sptSet[y] == False and \
                        dist[y] > dist[x] + self.graph[x][y]:
                    dist[y] = dist[x] + self.graph[x][y]
        self.printSolution(dist)
 
graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
         [4, 0, 8, 0, 0, 0, 0, 11, 0],
         [0, 8, 0, 7, 0, 4, 0, 0, 2],
         [0, 0, 7, 0, 9, 14, 0, 0, 0],
         [0, 0, 0, 9, 0, 10, 0, 0, 0],
         [0, 0, 4, 14, 10, 0, 2, 0, 0],
         [0, 0, 0, 0, 0, 2, 0, 1, 6],
         [8, 11, 0, 0, 0, 0, 1, 0, 7],
         [0, 0, 2, 0, 0, 0, 6, 7, 0]]

obj = Graph(9,graph)
obj.dijkstra(0)
