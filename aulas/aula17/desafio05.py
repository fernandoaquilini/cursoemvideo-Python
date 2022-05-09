lista = []
opcao = 'S'
while opcao not in 'Nn':
    valor = int(input('Digite um valor: '))
    lista.append(valor)
    print('Valor adicionado com sucesso!')
    opcao = str(input('Quer continuar? [S/N]: ')).strip().upper()
listaPar = []
listaImpar = []
for cont in range(0, len(lista)):
    if lista[cont] % 2 == 0:
        listaPar.append(lista[cont])
    else:
        listaImpar.append(lista[cont])
print(f'Lista Completa: {lista}!')
print(f'Lista Par: {listaPar}!')
print(f'Lista Ímpar: {listaImpar}!')
