from collections import defaultdict
import heapq

# min heap
class MinHeap:

	def __init__(self):
		self._queue = []
		self._index = 0

	def insert(self, item, priority):
		heapq.heappush(self._queue, (-priority, self._index, item))
		self._index += 1

	def remove(self):
		return heapq.heappop(self._queue)[-1]

	def get_length(self):
		return len(self._queue)

# grafo
class Graph:

	def __init__(self):
		self.graph = defaultdict(list)
		self.vertexes = {}

	def addEdge(self, src, dest, cost):
		self.graph[src].append((dest, cost))
		self.vertexes[src] = src
		self.vertexes[dest] = dest

	def dijkstra(self, src, dest):

		# obtém o número de vértices
		number_vertexes = len(self.vertexes)

		# estimativas de menor custo
		p = [None for i in range(number_vertexes)]

		# estima para origem é 0
		p[src] = 0

		# constrói a min heap
		min_heap = MinHeap()

		# insere a origem na min heap
		min_heap.insert(src, 0)

		# enquanto o tamanho da fila for maior que 0
		while min_heap.get_length() > 0:

			# remove da fila de prioridades
			u = min_heap.remove()

			# percorre os adjacentes de "u"
			for edge in self.graph[u]:

				# obtém o vértice adjacente e o custo
				v, cost = edge

				# relaxamento
				if p[v] is None or p[v] > p[u] + cost:

					# atualiza a estimativa de custo
					p[v] = p[u] + cost

					# insere na fila de prioridades
					min_heap.insert(v, p[v])

		# retorna o custo do menor caminho
		return p[dest]

g = Graph()

g.addEdge(0, 1, 1)
g.addEdge(0, 3, 3)
g.addEdge(0, 4, 10)
g.addEdge(1, 2, 5)
g.addEdge(2, 4, 1)
g.addEdge(3, 2, 2)
g.addEdge(3, 4, 6)

print(g.dijkstra(0, 4))