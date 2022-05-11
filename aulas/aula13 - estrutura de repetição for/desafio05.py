soma = 0
for cont in range(1, 6+1):
    numero = int(input('Digite o {}º número inteiro: '.format(cont)))
    if numero % 2 == 0:
        soma += numero
print('A soma de todos os números pares foi {}.'.format(soma))
