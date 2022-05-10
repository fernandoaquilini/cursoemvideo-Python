import moeda

valor = float(input('Digite um valor (R$): '))
print(f'A metade de {valor:.2f} é {moeda.metade(valor):.2f}')
print(f'O dobro de {valor:.2f} é {moeda.dobro(valor):.2f}')
print(f'Aumentando 10% {valor:.2f} é {moeda.aumentar(valor, 10):.2f}')
print(f'Reduzindo 13% de {valor:.2f} é {moeda.diminuir(valor, 13):.2f}')
