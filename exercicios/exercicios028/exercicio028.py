import random
from time import sleep
número = random.randint(1, 5)
resposta = int(input('Adivinhe o número: '))
print('Processando...')
sleep(2)
if número == resposta:
    print('Parabéns, você acertou!!')
else:
    print('Você errou!! A resposta era {}.'.format(número))
