# docstring
def contador(i, f, p):
    '''
    -> Faz uma contagem e mostra na tela.
        :param i: Início da contagem
        :param f:  Fim da contagem
        :param p: Passo da Contagem
        :return: Sem retorno
    '''
    c = i
    while c <= f:
        print(f'{c} ', end='')
        c += p
    print('FIM!')


contador(0, 100, 10)
help(contador)
