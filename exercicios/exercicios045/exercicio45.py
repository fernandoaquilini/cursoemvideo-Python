from random import randint
from time import sleep
computador = randint(0, 2)
jogador = int(input('0 - Pedra\n1 - Papel\n2 - Tesoura\nEscolha sua jogada: '))
print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PÔ!')
print('-='*20)
if computador == 0:
    if jogador == 0:
        print('Pedra com Pedra, deu empate!!')
    elif jogador == 1:
        print('Pedra com Papel, JOGADOR ganhou!!')
    elif jogador == 2:
        print('Pedra com Tesoura, COMPUTADOR ganhou!!')
    else:
        print('Jogador Burro! Escolheu errado!')
elif computador == 1:
    if jogador == 0:
        print('Papel com Pedra, COMPUTADOR ganhou!!')
    elif jogador == 1:
        print('Papel com Papel, deu empate!!')
    elif jogador == 2:
        print('Papel com Tesoura, JOGADOR ganhou!!')
    else:
        print('Jogador Burro! Escolheu errado!')
elif computador == 2:
    if jogador == 0:
        print('Tesoura com Pedra, JOGADOR ganhou!!')
    elif jogador == 1:
        print('Tesoura com Papel, COMPUTADOR ganhou!!')
    elif jogador == 2:
        print('Tesoura com Tesoura, deu empate!!')
    else:
        print('Jogador Burro! Escolheu errado!')
print('-='*20)