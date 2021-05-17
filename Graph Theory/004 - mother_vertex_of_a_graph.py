from collections import defaultdict

class Graph:
	def __init__(self, vertices):
		self.vertices = vertices
		self.adjacency_list = defaultdict(list)

	def add_edge(self, a, b):
		self.adjacency_list[a].append(b)

	def dfs_recursive(self, vertex, visited):
		if vertex not in visited:
			visited.append(vertex)
			# print(vertex, end =' ') # DFS of a graph 

			for neighbour in self.adjacency_list[vertex]:
				self.dfs_recursive(neighbour, visited)

	
	def mother_vertex(self):
		visited = []
		mother_vertex_index = 0
		for vertex in range(self.vertices):
			if vertex not in visited:
				self.dfs_recursive(vertex, visited)
				mother_vertex_index = vertex
		# check if our mother_vertex is actually reaching to every other vertex in our graph
		
		new_visited = list()
		self.dfs_recursive(mother_vertex_index, new_visited)
		if (len(new_visited) == self.vertices):
			print("MOTHER VERTEX of this GRAPH :", mother_vertex_index)
		else:
			print(-1)

		

if __name__ == '__main__':
	g = Graph(7)
	g.add_edge(0, 1)
	g.add_edge(0, 2)
	g.add_edge(1, 3)
	g.add_edge(4, 1)
	g.add_edge(6, 4)
	g.add_edge(5, 6)
	g.add_edge(5, 2)
	g.add_edge(6, 0)

	g.mother_vertex()
