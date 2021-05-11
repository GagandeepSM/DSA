from collections import defaultdict

class Graph:
	def __init__(self):
		self.adjacency_list = defaultdict(list)

	def addEdge(self, a, b):
		self.adjacency_list[a].append(b)
	
	def print(self):
		for node in self.adjacency_list.items():
			print(node)
	
	def bfs(self, start):
		stack = list()
		stack.append(start)
		ans = list()
		visited = [False] * len(self.adjacency_list)
		while stack:
			node = stack.pop(0)
			if visited[node] == False:
				stack.extend(self.adjacency_list[node])
				ans.append(node)
				visited[node] = True
		print(*ans)


if __name__ == '__main__':
	vertices = 3
	g = Graph()
	g.addEdge(0, 1)
	g.addEdge(0, 2)
	g.addEdge(1, 2)
	g.addEdge(2, 0)
	g.addEdge(2, 3)
	g.addEdge(3, 3)
	g.bfs(2)
