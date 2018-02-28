#cria dicionario
d = {}

d['vegeta'] = 10 #adiciona chave/valor
d['naruto'] = 20
d['goku'] = 30

print(d)

#percorre dicionario
for k in d.keys():
    print(d[k])

#deletar
del d['vegeta']

#verifica

if 'vegeta' in d.keys():
    print('chave encontrada')
else:
    print('nao encontrada')