pessoa = []
todos = []
while True:
    pessoa.append(str(input('Digite o nome: ')).strip().title())
    pessoa.append(float(input('Digite o peso (Kg): ')))
    todos.append(pessoa[:])
    pessoa.clear()
    opcao = str(input('Deseja continuar? [S/N]: ')).strip().upper()
    if opcao in 'N':
        break
print(f'você cadastrou {len(todos)} pessoas.')
maiorpeso = menorpeso = 0
for cont in range(0, len(todos)):
    if cont == 0:
        maiorpeso = menorpeso = todos[cont][1]
    else:
        if maiorpeso < todos[cont][1]:
            maiorpeso = todos[cont][1]
        if menorpeso > todos[cont][1]:
            menorpeso = todos[cont][1]
print(f'O maior peso foi {maiorpeso:.2f}Kg. Peso de', end='')
for p in todos:
    if p[1] == maiorpeso:
        print(f' {p[0]} ', end='')
print()
print(f'O menor peso foi {menorpeso:.2f}Kg. Peso de', end='')
for p in todos:
    if p[1] == menorpeso:
        print(f' {p[0]} ', end='')
print()
