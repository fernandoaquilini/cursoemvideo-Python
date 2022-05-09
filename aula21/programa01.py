# interactive help
# help()
# help(print)
# print(input.__doc__)

# argumentos opcionais
def somar(a=0, b=0, c=0):
    '''
    -> Faz a soma de três valores e mostra o resultado na tela.
        :param a: (Opcional). Se não atribuído, vale 0.
        :param b: (Opcional). Se não atribuído, vale 0.
        :param c: (Opcional). Se não atribuído, vale 0.
    :return: Sem retorno.

    Criada por: Fernando Aquilini
    '''
    s = a + b + c
    print(f'A soma vale {s}.')


help(somar)
print()
somar(1, 2, 3)
somar(8, 4)
somar()
somar(b=8, c=8)
somar(c=78, a=8)
