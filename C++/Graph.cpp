#include <iostream>
#include <list>
using namespace std;
class Graph {
    int numVertices;
    list<int> *adjLists;
    bool *visited;
    public:
        Graph(int vertices) {
            numVertices = vertices;
            adjLists = new list<int>[vertices];
            visited = new bool[vertices];
        }
        void addEdge(int src, int dest) {
            adjLists[src].push_front(dest);
            adjLists[dest].push_front(src);
        }
        void DFS(int vertex) {
            visited[vertex] = true;
            list<int> adjList = adjLists[vertex];
            cout << vertex << " ";
            list<int>::iterator i;
            for (i = adjList.begin(); i != adjList.end(); ++i) {
                if (!visited[*i]) {
                    DFS(*i);
                }
            }
        }
        void BFS(int startVertex) {
            visited = new bool[numVertices];
            for (int i = 0; i < numVertices; i++) {
                visited[i] = false;
            }
            list<int> queue;
            visited[startVertex] = true;
            queue.push_back(startVertex);
            list<int>::iterator i;
            while (!queue.empty()) {
                int currVertex = queue.front();
                cout << currVertex << " ";
                queue.pop_front();
                for (i = adjLists[currVertex].begin(); i != adjLists[currVertex].end(); ++i) {
                    int adjVertex = *i;
                    if (!visited[adjVertex]) {
                        visited[adjVertex] = true;
                        queue.push_back(adjVertex);
                    }
                }
            }
        }
};
int main() {
    Graph obj(7);
    int src;
    obj.addEdge(0, 1);
    obj.addEdge(0, 2);
    obj.addEdge(1, 3);
    obj.addEdge(1, 4);
    obj.addEdge(2, 5);
    obj.addEdge(2, 6);
    cout << "Enter the Source Vertex : ";
    cin>>src;
    cout << "\nDepth First Search from Vertex " << src << endl;
    obj.DFS(src);
    cout << "\nBreadth First Search from Vertex " << src << endl;
    obj.BFS(src);
    return 0;
}
