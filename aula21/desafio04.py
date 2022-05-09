# Functions
def leiaInt(msg):
    while True:
        n = str(input(msg))
        if n.strip().isnumeric():
            break
        else:
            print('ERRO! Digite o número novamente.')
    return int(n)


# Main
n = leiaInt('Digite um número: ')
print(f'Você digitou o número {n}')
