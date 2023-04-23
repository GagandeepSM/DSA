from collections import defaultdict

class Graph:
    def __init__(self, v):
        self.adj_list = defaultdict(list)
        self.vertices = v

    def add_edge(self, u, v):
        self.adj_list[u].append(v)

    def is_cyclic_util(self, node, visited, recursion_stack):
        visited[node] = True
        recursion_stack[node] = True
        
        for neighbours in self.adj_list[node]:
            if not visited[neighbours]:
                if self.is_cyclic_util(neighbours, visited, recursion_stack):
                    return True
            elif recursion_stack[neighbours]:
                return True
            
        recursion_stack[node] = False
        return False
        
    def is_cyclic(self):
        visited = [False] * self.vertices
        recursion_stack = [False] * self.vertices

        for node in self.adj_list:
            if not visited[node]:
                if self.is_cyclic_util(node, visited, recursion_stack):
                    print("Cycle Present")
                    break
        else:
            print("No Cycle Present!")
        

if __name__ == '__main__':
    g = Graph(4)
    g.add_edge(0,1)
    g.add_edge(0,2)
    g.add_edge(1,2)
    g.add_edge(2,0)
    g.add_edge(2,3)
    g.add_edge(3,3)

    g.is_cyclic()
