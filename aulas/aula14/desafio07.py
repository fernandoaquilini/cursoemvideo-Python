print('-' * 30)
print('Sequencia de Fibonacci')
print('-' * 30)
termos = int(input('Digite o número de Termos: '))
ant02 = 0
ant01 = 1
print('{} -> {}'.format(ant02, ant01), end='')
contador = 3
while contador <= termos:
    prox = ant01 + ant02
    print(' -> {}'.format(prox), end='')
    contador += 1
    ant02 = ant01
    ant01 = prox
print(' -> FIM!')
print('~' * 30)