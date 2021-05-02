class Graph:
    
    def __init__(self, N):
        self.n = N                                                      #Create a graph with 'N' vertices
        self.vertices = dict()                                          #Set vertices with their indices for Adjacency matrix
        self.total_vertices = [0]*N                                     #Keep track of total vertices and their index
        self.adj_matrix = [[-1]*N for _ in range(N)]                    #Adjacency Matrix
        
    def add_vertex(self, index, vertex):
        self.vertices[vertex] = index                                   #Add vertex with their index for matrix
        self.total_vertices[index] = vertex                             #Add vertex to total vertices 
        
    def add_edge(self, vertex_from, vertex_to, weight):
        i = self.vertices[vertex_from]                      
        j = self.vertices[vertex_to]
        self.adj_matrix[i][j] = weight
        self.adj_matrix[j][i] = weight                                  #In case of directed graph exclude this line of code
    
    def get_vertices(self):
        return self.total_vertices                                      #Return total vertices
    
    def get_edges(self):
        edges = []
        for row in range(self.n):
            for col in range(self.n):
                if self.adj_matrix[row][col] !=- 1:
                    edges.append((self.total_vertices[row], self.total_vertices[col], self.adj_matrix[row][col]))
        return edges
    
    def get_adjacency_matrix(self):
        return self.adj_matrix                                          #Return adjacency matrix
        
if __name__ == '__main__':
    
    number_of_vertices = 4
    graph_obj = Graph(number_of_vertices)
    
    vertices = ['a','b','c','d']                                        #Hardcoded vertices
    for index in range(number_of_vertices):
        graph_obj.add_vertex(index,vertices[index])                     #Update vertices in graph
        
    edges = [('a','b',1), ('b','c',2), ('c','d',3), ('d','a',4)]        #Hardcoded edges
    for edge in edges:
        graph_obj.add_edge(edge[0], edge[1], edge[2])                   #Update edges in graph

    print('VERTICES:')
    print(graph_obj.get_vertices())
    
    print('EDGES:')
    [print(edge) for edge in graph_obj.get_edges()]

    print('ADJACENCY MATRIX:')
    [print(row) for row in graph_obj.get_adjacency_matrix()]
        
        
        
        
        
        
        
        
        
            
    
