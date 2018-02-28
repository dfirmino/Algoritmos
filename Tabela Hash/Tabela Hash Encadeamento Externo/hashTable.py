#https://pt.wikibooks.org/wiki/Algoritmos/Estruturas_de_dados/Tabela_Hash
import sys
class HashTable:

    def __init__(self,tableSize):
        if tableSize < 1:
            print('Erro, tamanho da tabela tem que ser positivo')
            sys.exit(1)
        
        self.tableSize = tableSize
        self.table = [[] for i in range(tableSize)]

    def hashFunc(self,key):
        return key % self.tableSize

    def insert(self,key):
        self.table[self.hashFunc(key)].append(key)
    
    def show(self):
        
        for linked_list in self.table:
            if linked_list:
                for key in linked_list:
                    print('%d' % key, end=' ')
                print('')

    def search(self,key):
        if key in self.table[self.hashFunc(key)]:
            return True
        return False

d = HashTable(9)
d.insert(19)
d.insert(28)
d.insert(20)
d.insert(5)
d.insert(33)
d.insert(15)
d.show()