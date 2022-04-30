from random import randint
contador = 0
while True:
    computadorN = randint(0, 10)
    jogadorN = int(input('\nDigita o valor: '))
    while True:
        jogadorO = str(input('Par ou Ímpar [P/I]: ')).strip().upper()[0]
        if jogadorO in 'PI':
            break
    # print(f'Você: {jogadorN} + Comp: {computadorN} = {jogadorN + computadorN}.')
    if (computadorN + jogadorN) % 2 == 0:
        if jogadorO in 'P':
            print('-'*30)
            print(f'GANHOU! Você: {jogadorN} + Comp: {computadorN} = {jogadorN + computadorN}. É PAR')
            print('-' * 30)
            contador += 1
        else:
            print('-'*30)
            print(f'PERDEU! Você: {jogadorN} + Comp: {computadorN} = {jogadorN + computadorN}. É PAR')
            print('-' * 30)
            break
    else:
        if jogadorO in 'I':
            print('-'*30)
            print(f'GANHOU! Você: {jogadorN} + Comp: {computadorN} = {jogadorN + computadorN}. É ÍMPAR')
            print('-' * 30)
            contador += 1
        else:
            print('-'*30)
            print(f'PERDEU! Você: {jogadorN} + Comp: {computadorN} = {jogadorN + computadorN}. É ÍMPAR')
            print('-' * 30)
            break
print(f'GAME OVER! Você venceu {contador}x consecutivas')
