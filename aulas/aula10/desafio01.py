import random
numero = random.randint(1, 5)
resposta = int(input('Adivinhe o número: '))
if numero == resposta:
    print('Parabéns, você acertou!!')
else:
    print('Você errou!! A resposta era {}.'.format(numero))
