from collections import defaultdict

class Graph:

	def __init__(self):
		self.adjancency_list = defaultdict(list)

	def add_edge(self, a, b):
		self.adjancency_list[a].append(b)

	def dfs_iterative(self, s):  		
		#TO UPDATE
		stack = [];stack.append(s)
		visited = list()
		while stack:
			node = stack.pop()			
			if node not in visited:
				visited.append(node)

				for neighbour in reversed(self.adjancency_list[node]): #KEY POINT TO REVERSE THE LIST NODE TP GET
					if neighbour not in visited:
						stack.append(neighbour)
		print("DFS_ITERATIVE :", *visited)

	def dfs_recursive(self, start, visited):
		if start not in visited:
			print(start, end=" ")
			visited.append(start)

			for neighbour in self.adjancency_list[start]:
				self.dfs_recursive(neighbour, visited)

	def dfs_operations(self, start):
		visited = []
		print('DFS_RECURSIVE :', end=" ")
		self.dfs_recursive(start, visited)
		print()
		self.dfs_iterative(start)

if __name__ == '__main__':

	graph = Graph()
	graph.add_edge(0, 1)
	graph.add_edge(0, 2)
	graph.add_edge(1, 2)
	graph.add_edge(2, 0)
	graph.add_edge(2, 3)
	graph.add_edge(3, 3)

	graph.dfs_operations(2)
