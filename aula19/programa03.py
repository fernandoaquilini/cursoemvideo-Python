brasil = []
estado01 = {'nome': 'Rio de Janeiro', 'sigla': 'RJ'}
estado02 = {'nome': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado01)
brasil.append(estado02)
print(brasil)
print(brasil[0])
print(brasil[0]['nome'])
print(brasil[1]['sigla'])
estado = dict()
for cont in range(0, 1):
    estado['nome'] = str(input('Digite o nome do Estado: ')).strip().title()
    estado['sigla'] = str(input('Digite a sigla: ')).strip().upper()
    brasil.append(estado.copy())
print(brasil)
for e in brasil:
    for k, v in e.items():
        print(f'{k} = {v}')

