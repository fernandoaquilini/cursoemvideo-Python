def metade(v=0):
    resp = v / 2
    return resp


def dobro(v=0):
    resp = v * 2
    return resp


def aumentar(v=0, p=0):
    resp = v + (v * (p / 100))
    return resp


def diminuir(v=0, p=0):
    resp = v - (v * (p / 100))
    return resp


def moeda(p=0, m='R$ '):
    return f'{m}{p:.2f}'.replace('.', ',')
