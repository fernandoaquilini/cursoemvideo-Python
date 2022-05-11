from random import randint
from time import sleep
computador = randint(1, 10)
resposta = 0
contador = 0
while resposta != computador:
    resposta = int(input('Adivinhe o número [1..10]: '))
    contador += 1
    #print('Processando...')
    #sleep(2)
    if resposta != computador:
        print('Errou!')
print('Parabéns, você acertou com {} tentativas!! A resposta era {}.'.format(contador, computador))
