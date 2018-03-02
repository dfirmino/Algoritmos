class Grafo:

    def __init__(self,vertices):
        self.vertices = vertices
        self.grafo = [ [] for i in range(vertices)]

    def add_aresta(self,u,v):
        self.grafo[u -1].append(v - 1)

    def show(self):
        for i in range(self.vertices):
            print('%d: ' % (i + 1) , end=' ')
            for j in self.grafo[i]:
                print('%d ->' % (j + 1 ), end=' ')
            print('')        

g = Grafo(5)
g.add_aresta(1,2)
g.add_aresta(4,1)
g.add_aresta(2,3)
g.add_aresta(2,5)
g.add_aresta(5,3)
g.show()