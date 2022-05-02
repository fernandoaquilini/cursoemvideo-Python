pessoa = []
todos = []
maiorpeso = menorpeso = 0
while True:
    pessoa.append(str(input('Digite o nome: ')).strip().title())
    pessoa.append(float(input('Digite o peso (Kg): ')))
    if len(todos) == 0:
        maiorpeso = menorpeso = pessoa[1]
    else:
        if maiorpeso < pessoa[1]:
            maiorpeso = pessoa[1]
        if menorpeso > pessoa[1]:
            menorpeso = pessoa[1]
    todos.append(pessoa[:])
    pessoa.clear()
    opcao = str(input('Deseja continuar? [S/N]: ')).strip().upper()
    if opcao in 'N':
        break
print(f'você cadastrou {len(todos)} pessoas.')
print(f'O maior peso foi {maiorpeso:.2f}Kg. Peso de', end='')
for p in todos:
    if p[1] == maiorpeso:
        print(f' [{p[0]}] ', end='')
print()
print(f'O menor peso foi {menorpeso:.2f}Kg. Peso de', end='')
for p in todos:
    if p[1] == menorpeso:
        print(f' [{p[0]}] ', end='')
print()
