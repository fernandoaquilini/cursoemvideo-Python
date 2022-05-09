from time import sleep


def contagem(start, end, step):
    print(f'Contagem de {start} até {end} de {abs(step)} em {abs(step)}!')
    if step == 0:
        if start > end:
            step = -1
        else:
            step = 1
    if step > 0:
        end += 1
    else:
        end -= 1
    linha()
    for c in range(start, end, step):
        print(f'{c} ', end='')
        # sleep(0.5)
    print('FIM!')


def linha():
    print('-=' * 20)


contagem(1, 10, 1)
contagem(10, 0, -2)
print('Agora é a sua vez de personalizar a contagem!')
ini = int(input('Início: '))
fim = int(input('Fim: '))
pas = int(input('Passo: '))
contagem(ini, fim, pas)
