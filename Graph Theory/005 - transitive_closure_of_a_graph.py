from collections import defaultdict

class Graph:

	def __init__(self, vertices):
		self.V = vertices

	def transitiveClosure(self,graph):

		reach =graph.copy()
		for k in range(self.V):
			for i in range(self.V):
				for j in range(self.V):
					reach[i][j] = reach[i][j] or (reach[i][k] and reach[k][j])
		print(reach)
		
g = Graph(4)

graph = [[1, 1, 0, 1],
		[0, 1, 1, 0],
		[0, 0, 1, 1],
		[0, 0, 0, 1]]

g.transitiveClosure(graph)
