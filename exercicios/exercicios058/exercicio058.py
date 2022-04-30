from random import randint
from time import sleep
computador = randint(1, 1000)
resposta = 0
contador = 0
while resposta != computador:
    resposta = int(input('Adivinhe o número [1..1000]: '))
    contador += 1
    #print('Processando...')
    #sleep(2)
    if resposta != computador:
        print('Errou! ', end='')
        if resposta < computador:
            print('É mais!!')
        else:
            print('É menos!!')
print('Parabéns, você acertou com {} tentativas!! A resposta era {}.'.format(contador, computador))
