from math import factorial
numero = int(input('Digite um número: '))
print('{}! é igual a {}.'.format(numero, factorial(numero)))

'''fatorial = 1
numero = int(input('Digite um número: '))
for cont in range(fatorial, numero+1):
    fatorial *= cont
print('{}! é igual a {}!'.format(numero, fatorial))'''

fatorial = 1
numero = int(input('Digite um número: '))
print('Calculando o {}! = '.format(numero))
contador = numero
while contador > 0:
    print(' {} '.format(contador), end='')
    print('x' if contador > 1 else '=', end='')
    fatorial *= contador
    contador -= 1
print(' {}. '.format(fatorial))
