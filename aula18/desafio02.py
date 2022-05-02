listaPar = []
listaImpar = []
listaGeral = []
listaGeral.append(listaPar)
listaGeral.append(listaImpar)
for cont in range(0, 11):
    valor = int(input('Digite um número inteiro: '))
    if valor % 2 == 0:
        listaPar.append(valor)
    else:
        listaImpar.append(valor)
listaPar.sort()
listaImpar.sort()
print(f'Estes foram os números pares: {listaGeral[0]}')
print(f'Estes foram os números ímpares: {listaGeral[1]}')
print(f'E estas são as duas, uma do lado da outra: {listaGeral}')
