from collections import defaultdict


class Graph:

    def __init__(self, vertices):
        self.vertices = vertices
        self.adj_list = defaultdict(list)

    def add_edge(self, u, v):
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)

    def is_cyclic_util(self, node, visited, parent):
        visited[node] = True
        
        for neighbour in self.adj_list[node]:
            if visited[neighbour] == False:
                if self.is_cyclic_util(neighbour, visited, node):
                    return True
            elif parent != neighbour:
                return True
        return False

    def is_cyclic(self):
        visited = [False] * self.vertices

        for node in range(self.vertices):
            if visited[node] == False:
                if self.is_cyclic_util(node, visited, -1):
                    print("Cycle Present")
                    break
        else:
            print("No Cycle Present!")

if __name__ == '__main__':
    g = Graph(5)
    g.add_edge(0, 1)
    g.add_edge(1, 2)

    g.is_cyclic()
