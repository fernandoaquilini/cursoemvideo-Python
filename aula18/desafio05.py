from random import randint
from time import sleep
print('-' * 30)
print(f'{"JOGOS DA MEGA SENA":^30}')
print('-' * 30)
jogos = int(input('Quantos jogos gostaria que eu sorteasse? '))
linha = []
matriz = []
for j in range(0, jogos):
    while len(linha) < 6:
        numero = (randint(1, 60))
        if numero not in linha:
            linha.append(numero)
    matriz.append(linha[:])
    linha.clear()
# print(matriz)
print(f'{"-=" * 3} SORTEANDO {jogos} JOGOS! {"-=" * 3}')
for c, l in enumerate(matriz):
    sleep(1)
    l.sort()
    print(f'Jogo {c+1}: {l}')
print(f'{"-=" * 5} BOA SORTE! {"-=" * 5}')
