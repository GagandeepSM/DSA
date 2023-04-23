from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adj_list = defaultdict(list)

    def add_edge(self, u, v):
        self.adj_list[u].append(v)

    def is_cyclic_util(self, node, color):
        color[node] = 'Gray'
        for neighbour in self.adj_list[node]:
            if color[neighbour] == 'White':
                if self.is_cyclic_util(neighbour, color):
                    return True
            elif color[neighbour] == 'Gray':
                return True
        color[node] = 'Black'
        return False
        
    def is_cyclic(self):
        color = ['White'] * self.vertices
        for node in range(self.vertices):
            if color[node] == 'White':
                if self.is_cyclic_util(node, color):
                    print('Cycle Present')
                    break
        else:
            print('No cycle present!')
    
if __name__ == "__main__":
    g = Graph(4)
    g.add_edge(0,1)
    g.add_edge(0,2)
    g.add_edge(1,2)
    g.add_edge(2,0)
    g.add_edge(2,3)
    g.add_edge(3,3)
    g.is_cyclic()
