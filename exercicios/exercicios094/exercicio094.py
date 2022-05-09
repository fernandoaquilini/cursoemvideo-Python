pessoa = {}
lista = []
somaIdade = somaMulher = somaHomem = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Digite o nome: ')).strip().title()
    while True:
        pessoa['sexo'] = str(input('Digite o sexo: ')).strip().upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Opção incorreta!')
    if pessoa['sexo'] == 'M':
        somaHomem += 1
    else:
        somaMulher += 1
    pessoa['idade'] = int(input('Digite a idade: '))
    somaIdade += pessoa['idade']
    lista.append(pessoa.copy())
    while True:
        opcao = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
        if opcao in 'SN':
            break
        print('ERRO! Opção incorreta!')
    if opcao == 'N':
        break
print(lista)
print('-=' * 20)
print(f'- Você cadastrou {len(lista)} pessoa(s) na lista.')
print(f'- A média de idade do grupo foi {(somaIdade / len(lista)):.2f}.')
print('-=' * 20)
print(f'- Divididos entre {somaHomem} homem(ns) e {somaMulher} mulher(es).')
print('Homem(ns): ')
for ps in lista:
    if ps['sexo'] in 'Mm':
        print(f'  -> {ps["nome"]}, de {ps["idade"]} anos.')
print('Mulher(es): ')
for ps in lista:
    if ps['sexo'] in 'Ff':
        print(f'  -> {ps["nome"]}, de {ps["idade"]} anos.')
print('-=' * 20)
print(f'- E com algum(as) pessoa(s) com idade acima da média.')
for ps in lista:
    if ps['idade'] > (somaIdade / len(lista)):
        print(f'  -> {ps["nome"]}, de {ps["idade"]} anos.')
print('-=' * 20)
