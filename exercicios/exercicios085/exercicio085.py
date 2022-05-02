lista = [[], []]
for cont in range(0, 11):
    valor = int(input('Digite um número inteiro: '))
    if valor % 2 == 0:
        lista[0].append(valor)
    else:
        lista[1].append(valor)
lista[0].sort()
lista[1].sort()
print(f'Estes foram os números pares: {lista[0]}')
print(f'Estes foram os números ímpares: {lista[1]}')
print(f'E estas são as duas, uma do lado da outra: {lista}')
