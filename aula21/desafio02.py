# Functions
def fatorial(f=1, show=False):
    """
    -> Calcula o Fatorial de um número Inteiro.
        :param f: O número a ser calculado (INT)
        :param show: (OPCIONAL). Mostrar ou não a conta.
        :return: O Valor do Fatorial do Número f.
    """
    resp = 1
    for c in range(f, 0, -1):
        if show:
            print(f'{c}', end='')
            if c == 1:
                print(' = ', end='')
            else:
                print(' X ', end='')
        resp *= c
    return resp


# Main

print(f'{fatorial(1)}')
print(f'{fatorial(5)}')
print(f'{fatorial(10, True)}')
help(fatorial)
