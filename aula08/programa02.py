from math import sqrt, ceil, floor
num = int(input('Digite um número qualquer: '))
raiz = sqrt(num)
print('A raiz quadrada de {} é igual a {}'.format(num, raiz))
print('A raiz quadrada de {} é igual a {:.5f}'.format(num, raiz))
print('A raiz quadrada de {}, arredondando para cima é igual a {}'.format(num, ceil(raiz)))
print('A raiz quadrada de {}, arredondando para baixo é igual a {}'.format(num, floor(raiz)))
