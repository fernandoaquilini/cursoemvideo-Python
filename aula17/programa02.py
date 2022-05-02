num = [2, 5, 9, 1]
print(num)
num[2] = 3
print(num)
num.append(7)
print(num)
num.sort(reverse=True)
num.sort()
print(num)
print(f'Esta lista tem {len(num)} elementos...')
num.insert(2, 0)
print(num)
num.pop()
num.pop(2)
print(num)

num.insert(2, 2)
print(num)
num.remove(2)
print(num)

if 4 in num:
    num.remove(4)
    print(num)
else:
    print('Não achei o 4!')

if 5 in num:
    num.remove(5)
    print(num)
else:
    print('Não achei o 5!')

valores = []
valores.append(5)
valores.append(9)
valores.append(4)
for v in valores:
    print(f'{v}...')

for c, v in enumerate(valores):
    print(f'Na posição {c} está o valor {v}.')
    print(f'Na {c+1}ª posição está o valor {v}.')

outrosValores = list()
for cont in range(0, 5):
    outrosValores.append(int(input('Digite um valor: ')))

for c, v in enumerate(outrosValores):
    print(f'Na posição {c} está o valor {v}.')
    print(f'Na {c+1}ª posição está o valor {v}.')

listaA = [1, 2, 3, 4]
listaB = listaA
listaB.append(5)
print(f'Lista A: {listaA}')
print(f'Lista B: {listaB}')


listaA = [1, 2, 3, 4]
listaB = listaA[:]
listaB.append(5)
print(f'Lista A: {listaA}')
print(f'Lista B: {listaB}')
