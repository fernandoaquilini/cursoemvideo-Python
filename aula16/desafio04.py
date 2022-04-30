val01 = int(input('Digite o valor 01: '))
val02 = int(input('Digite o valor 02: '))
val03 = int(input('Digite o valor 03: '))
val04 = int(input('Digite o valor 04: '))

tupla = (val01, val02, val03, val04)
print(f'Você digitou {tupla}...')

cont9 = 0
for cont in range(0, len(tupla)):
    if tupla[cont] == 9:
        cont9 += 1
print(f'Apareceram {cont9} número(s) 9!')

print(f'A primeira posição com um número 3 é a {tupla.index(3) + 1}ª!')

print(f'Apareceram os seguintes números pares: [', end='')
for cont in range(0, len(tupla)):
    if tupla[cont] % 2 == 0:
        print(f' {tupla[cont]} ', end='')
print('].')

