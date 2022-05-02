dados = []
dados.append('Pedro')
dados.append(25)
print(dados)
print(dados[0])
print(dados[1])

pessoas = list()
pessoas.append(dados[:])
print(pessoas)
print(pessoas[0])
pessoas.append(['Maria', 19])
pessoas.append(['João', 32])
print(pessoas)
print(pessoas[0][0])
print(pessoas[1][1])
print(pessoas[2][0])

