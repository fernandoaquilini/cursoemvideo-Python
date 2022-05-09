# Functions
def header(msg):
    print('\033[0;30;42m~' * (len(msg) + 4))
    print(f'{msg:^{len(msg) + 4}}')
    print('~' * (len(msg) + 4))


def footer(msg):
    print('\033[0;30;41m~' * (len(msg) + 4))
    print(f'{msg:^{len(msg) + 4}}')
    print('~' * (len(msg) + 4))


def content(command, msg):
    print('\033[0;30;44m~' * (len(msg) + len(command) + 5))
    print(f'{f"{msg} {command.upper()}":^{len(msg) + len(command) + 5}}')
    print('~' * (len(msg) + len(command) + 5))


def rodaHelp(command):
    print('\033[1;30;47m')
    help(command)


# Main
comando = ''
while comando != 'fim':
    header('SISTEMA DE AJUDA DO PyHELP')
    comando = str(input('\033[mFunção ou Biblioteca > ')).strip().lower()
    if comando == 'fim':
        footer('ATÉ LOGO!')
        break
    else:
        content(comando, 'ACESSANDO O CONTEÚDO DO COMANDO')
        rodaHelp(comando)
