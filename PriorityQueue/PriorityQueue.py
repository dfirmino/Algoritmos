#Implementação da PQ com lista ordenada

class Person:
    def __init__(self,name,prior):
        self.name = name
        self.prior = prior
    
    def getName(self):
        return self.name
    
    def getPrior(self):
        return self.prior
    
class PriorityQueue:
    def __init__(self):
        self.pq = []
        self.len = 0
    
    #insere decrescentemente pela prioridade
    def push(self,person):
        if self.empty():
            self.pq.append(person)
        else:
            #procura-se onde inserir para manter a fila ordenada
            flag_push = False
            for i in range(self.len):
                if self.pq[i].getPrior() < person.getPrior():
                    self.pq.insert(i,person)
                    flag_push = True
                    break
            
            if not flag_push:
                #Insere ao final
                self.pq.insert(self.len,person)
            
        self.len += 1
    
    #remover
    def pop(self):
        if not self.empty():
            self.pq.pop(0)
            self.len -= 1
    
    def empty(self):
        if self.len == 0:
            return True
        return False

    def show(self):
        for p in self.pq:
            print('Nome %s' % p.getName())
            print('Prioridade %d' % p.getPrior())

#criando os objetos person
p1 = Person('Davi',28)
p2 = Person('Batman',23)
p3 = Person('Naruto',21)
p4 = Person('Goku',666)

#criando fila e inserindo elementos
pq = PriorityQueue()
pq.push(p1)
pq.push(p2)
pq.push(p3)
pq.push(p4)

#exibindo
pq.show()

#removendo
pq.pop()
pq.pop()
print('....Removendo....')
pq.show()
print('....Inserindo....')
pq.push(Person('Python',22))
pq.show()