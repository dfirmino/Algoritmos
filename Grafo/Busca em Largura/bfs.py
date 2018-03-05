class Grafo:

	def __init__(self, vertices):
		self.vertices = vertices
		self.grafo = [[0] * vertices for i in range(vertices)]

	def add_aresta(self, u, v):
		self.grafo[u - 1][v - 1] = 1
		self.grafo[v - 1][u - 1] = 1

	def show(self):
		for i in self.grafo:
			for j in i:
				print(j, end=' ')
			print('')

	def tem_ligacao(self, u, v):
		if self.grafo[u - 1][v - 1] == 1:
			return True
		return False

	def bfs(self, v):

		# lista de visitados
		visitados = [False] * self.vertices
		# marca 'v' como visitado
		visitados[v - 1] = True
		# insere 'v' na fila
		fila = [v - 1]

		print('%d visitado' % v)

		# enquanto a fila não for vazia
		while len(fila) > 0:

			# obtém o elemento da fila
			v = fila[0]

			# para cada vértice 'u' adjacente a 'v'
			for u in range(self.vertices):
				# verifica se existe conexão
				if self.grafo[v][u] == 1:
					# verifica se 'u' não foi visitado
					if visitados[u] == False:
						# marca 'u' como visitado
						visitados[u] = True
						# insere 'u' na fila
						fila.append(u)
						# imprime o elemento visitado
						print('%d visitado' % (u + 1))

			# remove 'v' da fila
			fila.pop(0)

g = Grafo(10)

g.add_aresta(1, 2)
g.add_aresta(1, 3)
g.add_aresta(1, 4)
g.add_aresta(2, 5)
g.add_aresta(3, 6)
g.add_aresta(3, 7)
g.add_aresta(4, 8)
g.add_aresta(5, 9)
g.add_aresta(6, 10)

g.bfs(1)