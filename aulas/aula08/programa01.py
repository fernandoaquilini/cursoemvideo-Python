import math
num = int(input('Digite um número qualquer: '))
raiz = math.sqrt(num)
print('A raiz quadrada de {} é igual a {}'.format(num, raiz))
print('A raiz quadrada de {} é igual a {:.5f}'.format(num, raiz))
print('A raiz quadrada de {}, arredondando para cima é igual a {}'.format(num, math.ceil(raiz)))
print('A raiz quadrada de {}, arredondando para baixo é igual a {}'.format(num, math.floor(raiz)))
