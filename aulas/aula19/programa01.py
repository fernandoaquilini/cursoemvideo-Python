# dados = dict()
dados = {'nome': 'Pedro', 'idade': 25}
print(dados['nome'])
print(dados['idade'])
dados['sexo'] = 'M'
print(dados)
del dados['idade']
print(dados)

filme = {'titulo': 'Star Wars',
         'ano': 1977,
         'diretor': 'George Lucas'
}
print(filme)
print(filme.values())
print(filme.keys())
print(filme.items())
for k, v in filme.items():
    print(f'O {k.title()} é {v}')

