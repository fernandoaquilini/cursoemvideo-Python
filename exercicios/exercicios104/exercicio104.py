# Functions
def leiaInt(msg):
    while True:
        n = str(input(msg))
        if n.strip().isnumeric():
            break
        else:
            print('\033[0;31mERRO! Digite o número novamente.\033[m')
    return int(n)


# Main
n = leiaInt('Digite um número: ')
print(f'Você digitou o número {n}')
