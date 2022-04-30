tupla = (int(input('Digite o valor 01: ')),
         int(input('Digite o valor 02: ')),
         int(input('Digite o valor 03: ')),
         int(input('Digite o valor 04: ')))
print(f'Você digitou {tupla}...')
print(f'Apareceram {tupla.count(9)} número(s) 9!')
if 3 in tupla:
    print(f'A primeira posição com um número 3 é a {tupla.index(3) + 1}ª!')
else:
    print('O número 3 não foi digitado nenhuma vez!')
print(f'Apareceram os seguintes números pares: [', end='')
for cont in range(0, len(tupla)):
    if tupla[cont] % 2 == 0:
        print(f' {tupla[cont]} ', end='')
print('].')

