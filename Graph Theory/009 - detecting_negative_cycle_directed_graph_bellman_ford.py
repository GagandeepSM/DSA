class Edge:
    def __init__(self):
        self.src = 0
        self.dest = 0
        self.weight = 0

class Graph:
    def __init__(self):
        self.V = 0
        self.E = 0
        self.edge = None

def create_graph(V,E):
    graph = Graph()
    graph.V = V
    graph.E = E
    graph.edge = [Edge() for i in range(E)]
    return graph

    
def is_negative_cycle_bellman_ford(graph, src):
    V = graph.V
    E = graph.E
    dist = [10000 for _ in range(V)]
    dist[src] = 0

    for i in range(1,V):
        for j in range(E):
            u = graph.edge[j].src
            v = graph.edge[j].dest
            wt = graph.edge[j].weight
            if( dist[u]+wt < dist[v] and dist!=10000):
                dist[v] = dist[u]+wt

    for j in range(E):
        u = graph.edge[j].src
        v = graph.edge[j].dest
        wt = graph.edge[j].weight
        if( dist[u]+wt < dist[v] and dist!=10000):
            return True
    return False
    

if __name__ == '__main__':
    V = 5; # Number of vertices in graph
    E = 8; # Number of edges in graph
    graph = create_graph(V, E);
 
    # add edge 0-1 
    graph.edge[0].src = 0;
    graph.edge[0].dest = 1;
    graph.edge[0].weight = -1;
 
    # add edge 0-2 
    graph.edge[1].src = 0;
    graph.edge[1].dest = 2;
    graph.edge[1].weight = 4;
 
    # add edge 1-2 
    graph.edge[2].src = 1;
    graph.edge[2].dest = 2;
    graph.edge[2].weight = 3;
 
    # add edge 1-3 
    graph.edge[3].src = 1;
    graph.edge[3].dest = 3;
    graph.edge[3].weight = 2;
 
    # add edge 1-4 
    graph.edge[4].src = 1;
    graph.edge[4].dest = 4;
    graph.edge[4].weight = 2;

    # add edge 3-2 
    graph.edge[5].src = 3;
    graph.edge[5].dest = 2;
    graph.edge[5].weight = 5;
 
    # add edge 3-1 
    graph.edge[6].src = 3;
    graph.edge[6].dest = 1;
    graph.edge[6].weight = 1;
 
    # add edge 4-3 
    graph.edge[7].src = 4;
    graph.edge[7].dest = 3;
    graph.edge[7].weight = -3;

    if (is_negative_cycle_bellman_ford(graph, 0)):
        print("Yes")
    else:
        print("No")
