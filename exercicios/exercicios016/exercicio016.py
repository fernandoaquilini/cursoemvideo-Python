'''numero = float(input('Digite um número Real qualquer: '))
print('A parte inteira de {} é igual a {}'.format(numero, int(numero)))'''

from math import trunc
numero = float(input('Digite um número Real qualquer: '))
print('A parte inteira de {} é igual a {}'.format(numero, trunc(numero)))
