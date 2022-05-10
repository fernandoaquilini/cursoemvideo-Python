def metade(v=0.0, f=False):
    resp = v / 2
    return resp if f is False else moeda(resp)


def dobro(v=0.0, f=False):
    resp = v * 2
    return resp if f is False else moeda(resp)


def aumentar(v=0.0, p=0.0, f=False):
    resp = v + (v * (p / 100))
    return resp if f is False else moeda(resp)


def diminuir(v=0.0, p=0.0, f=False):
    resp = v - (v * (p / 100))
    return resp if f is False else moeda(resp)


def moeda(p=0.0, m='R$ '):
    return f'{m}{p:.2f}'.replace('.', ',')


def resumo(p=0.0, a=0, r=0):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado: \t{moeda(p)}')
    print(f'Dobro do Preço: \t{dobro(p, True)}')
    print(f'Metade do Preço: \t{metade(p, True)}')
    print(f'Aumento de {a}%: \t{aumentar(p, a, True)}')
    print(f'Redução de {r}%: \t{diminuir(p, r, True)}')
    print('-' * 30)
