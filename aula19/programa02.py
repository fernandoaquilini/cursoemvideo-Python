pessoas = {'nome': 'Fernando', 'sexo': 'M', 'idade': 45}
print(pessoas)
print(pessoas['idade'])
print(f"O {pessoas['nome'].title()} tem {pessoas['idade']} anos.")
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
for k, v in pessoas.items():
    print(f'{k.title()} = {v}')
print('-' * 20)
pessoas['nome'] = 'Aurélio'
pessoas['idade'] = 17
print(pessoas)
print('-' * 20)
pessoas['peso'] = 115.5
print(pessoas)
print('-' * 20)
del pessoas['sexo']
for k, v in pessoas.items():
    print(f'{k.title()} = {v}')
