from random import randint
from time import sleep

def adiciona():
    val = []
    print('Adicionando os valores: ', end='')
    for c in range(0, 5):
        val.append(randint(1, 10))
        print(f' {val[c]} ', end='')
        sleep(0.2)
    print(' PRONTO!')
    return val


def somaPares(val):
    soma = 0
    for c in range(0, len(val)):
        if val[c] % 2 == 0:
            soma += val[c]
    return soma


valores = adiciona()
print(f'Somando os valores pares de {valores}, temos {somaPares(valores)}.')



