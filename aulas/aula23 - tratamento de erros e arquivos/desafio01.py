# Functions
def leiaint(msg):
    while True:
        try:
            v = int(input(msg))
        except (ValueError, TypeError) as erro:
            print(f'\033[0;31mERRO {erro.__class__}! Digite o número novamente.\033[m')
            continue
        except KeyboardInterrupt as erro:
            print(f'\033[0;31mERRO {erro.__class__}! Usuário cancelou a excecução.\033[m')
            return 0
        else:
            return v


def leiafloat(msg):
    while True:
        try:
            v = float(input(msg))
        except (ValueError, TypeError) as erro:
            print(f'\033[0;31mERRO {erro.__class__}! Digite o número novamente.\033[m')
            continue
        except KeyboardInterrupt as erro:
            print(f'\033[0;31mERRO {erro.__class__}! Usuário cancelou a excecução.\033[m')
            return 0.0
        else:
            return v


# Main
i = leiaint('Digite um número inteiro: ')
f = leiafloat('Digite um número float: ')
print(f'Você digitou o número inteiro {i} e o número float {f:.2f}')
