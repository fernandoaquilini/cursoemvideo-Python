dinheiro = float(input('Quanto você tem na sua carteira? '))
COTACAO = 3.27
print('Com R${:.2f} é possível você comprar US${:.2f}.'.format(dinheiro, dinheiro/COTACAO))
