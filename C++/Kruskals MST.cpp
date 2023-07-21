#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;
#define edge pair<int, int>
class Kruskals {
	private:
  		vector<pair<int, edge> > G;
  		vector<pair<int, edge> > T;
  		int *parent;
  		int V;
   	public:
  		Kruskals(int V) {
  			parent = new int[V];
  			for (int i = 0; i < V; i++) {
    			parent[i] = i;
    		}
  			G.clear();
  			T.clear();
		}
  		void AddWeightedEdge(int u, int v, int w) {
  			G.push_back(make_pair(w, edge(u, v)));
		}
  		int find_set(int i) {
  			if (i == parent[i]) {
    			return i;
    		}
  			else {
    			return find_set(parent[i]);
			}
		}
  		void union_set(int u, int v) {
  			parent[u] = parent[v];
		}
  		void kruskal() {
  			int i, uRep, vRep;
  			sort(G.begin(), G.end());
  			for (i = 0; i < G.size(); i++) {
    			uRep = find_set(G[i].second.first);
    			vRep = find_set(G[i].second.second);
    			if (uRep != vRep) {
      				T.push_back(G[i]);
      				union_set(uRep, vRep);
    			}
  			}
		}
  		void print() {
  			cout << " Edge :" << " Weight" << endl;
  			for (int i = 0; i < T.size(); i++) {
    			cout << T[i].second.first << " - " << T[i].second.second << " :   " << T[i].first;
    			cout << endl;
			}
		}
};
int main() {
	Kruskals obj(6);
  	obj.AddWeightedEdge(0, 1, 4);
  	obj.AddWeightedEdge(0, 2, 4);
  	obj.AddWeightedEdge(1, 2, 2);
  	obj.AddWeightedEdge(1, 0, 4);
  	obj.AddWeightedEdge(2, 0, 4);
  	obj.AddWeightedEdge(2, 1, 2);
  	obj.AddWeightedEdge(2, 3, 3);
  	obj.AddWeightedEdge(2, 5, 2);
  	obj.AddWeightedEdge(2, 4, 4);
  	obj.AddWeightedEdge(3, 2, 3);
	obj.AddWeightedEdge(3, 4, 3);
  	obj.AddWeightedEdge(4, 2, 4);
  	obj.AddWeightedEdge(4, 3, 3);
  	obj.AddWeightedEdge(5, 2, 2);
  	obj.AddWeightedEdge(5, 4, 3);
  	obj.kruskal();
  	obj.print();
  	return 0;
}
