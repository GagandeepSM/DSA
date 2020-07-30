class Graph:
    def __init__(self, nodes):
        self.adj_list = [[str(iterator)] for iterator in range(nodes)]
    
    def add_edge(self, frm, to):
        self.adj_list[frm].append(str(to))
        self.adj_list[to].append(str(frm))
    
    def get_adj_list(self):
        return self.adj_list
        
#Driver Code
if __name__ == "__main__": 
    V = 5
    graph = Graph(V) 
    graph.add_edge(0, 1) 
    graph.add_edge(0, 4) 
    graph.add_edge(1, 2) 
    graph.add_edge(1, 3) 
    graph.add_edge(1, 4) 
    graph.add_edge(2, 3) 
    graph.add_edge(3, 4) 
  
    print(graph.get_adj_list())
