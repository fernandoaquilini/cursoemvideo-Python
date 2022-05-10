def metade(v=0, f=False):
    resp = v / 2
    return resp if f is False else moeda(resp)


def dobro(v=0, f=False):
    resp = v * 2
    return resp if f is False else moeda(resp)


def aumentar(v=0, p=0, f=False):
    resp = v + (v * (p / 100))
    return resp if f is False else moeda(resp)


def diminuir(v=0, p=0, f=False):
    resp = v - (v * (p / 100))
    return resp if f is False else moeda(resp)


def moeda(p=0.0, m='R$ '):
    return f'{m}{p:.2f}'.replace('.', ',')
