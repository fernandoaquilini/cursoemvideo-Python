from time import sleep
c = ('\033[m',           # 0 - sem cores
     '\033[0;30;41m',    # 1 - vermelho
     '\033[0;30;42m',    # 2 - verde
     '\033[0;30;43m',    # 3 - amarelo
     '\033[0;30;44m',    # 4 - azul
     '\033[0;30;45m',    # 5 - roxo
     '\033[1;30;47mm',       # 6 - branco
     )


# Functions
def título(msg, cor):
    print(c[cor], end='')
    print('~' * (len(msg) + 4))
    print(f'{msg:^{len(msg) + 4}}')
    print('~' * (len(msg) + 4))
    print(c[0], end='')
    sleep(1)


def ajuda(command):
    título(f'Acessando o manual do comando \'{command}\'', 4)
    print(c[6], end='')
    help(command)
    print(c[0], end='')
    sleep(2)


# Main
comando = ''
while comando != 'fim':
    título('SISTEMA DE AJUDA DO PyHELP', 2)
    comando = str(input('\033[mFunção ou Biblioteca > ')).strip().lower()
    if comando == 'fim':
        break
    else:
        ajuda(comando)
título('ATÉ LOGO!', 1)

