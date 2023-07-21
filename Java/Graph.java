import java.util.*;
class Graph {
    private int V;
    private LinkedList<Integer> adj[];
    private boolean visited[];
    Graph(int vertices) {
        V = vertices;
        adj = new LinkedList[vertices];
        visited = new boolean[vertices];
        for (int i = 0; i < vertices; i++)
            adj[i] = new LinkedList<Integer>();
    }
    void addEdge(int src, int dest) {
        adj[src].add(dest);
        adj[dest].add(src);
    }
    void DFS(int vertex) {
        visited[vertex] = true;
        System.out.print(vertex + " ");
        Iterator<Integer> i = adj[vertex].listIterator();
        while (i.hasNext()) {
            int val = i.next();
            if (!visited[val])
                DFS(val);
        }
    }
    void BFS(int s) {
        boolean visited[] = new boolean[V];
        LinkedList<Integer> queue = new LinkedList();
        visited[s] = true;
        queue.add(s);
        while (queue.size() != 0) {
            s = queue.poll();
            System.out.print(s + " ");
            Iterator<Integer> i = adj[s].listIterator();
            while (i.hasNext()) {
                int n = i.next();
                if (!visited[n]) {
                    visited[n] = true;
                    queue.add(n);
                }
            }
        }
    }
    public static void main(String args[]) {
        Scanner s = new Scanner(System.in);
        Graph obj = new Graph(7);
        int src;
        obj.addEdge(0, 1);
        obj.addEdge(0, 2);
        obj.addEdge(1, 3);
        obj.addEdge(1, 4);
        obj.addEdge(2, 5);
        obj.addEdge(2, 6);
        System.out.print("Enter the Source Vertex : ");
        src = s.nextInt();
        System.out.print("\nDepth First Search from Vertex " + src + "\n");
        obj.DFS(src);
        System.out.print("\n");
        System.out.print("\nBreadth First Search from Vertex " + src + "\n");
        obj.BFS(src);
    }
}