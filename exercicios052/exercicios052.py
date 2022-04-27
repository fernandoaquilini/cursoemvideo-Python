from math import sqrt
número = int(input('Digite um número inteiro qualquer: '))
multiplos = 0
for cont in range(1, número+1):
    if número % cont == 0:
        if cont != 1 and cont != número:
            multiplos = multiplos + 1
if multiplos > 0:
    print('O número {} NÃO É PRIMO, porque possuí outros {} divisores!'.format(número, multiplos))
else:
    print('O número {} É PRIMO'.format(número))
