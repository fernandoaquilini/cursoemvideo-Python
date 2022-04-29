soma = 0
total = 0
for cont in range(1, 6+1):
    numero = int(input('Digite o {}º número inteiro: '.format(cont)))
    if numero % 2 == 0:
        soma += numero
        total = total + 1
print('A soma de todos os {} números pares foi {}.'.format(total, soma))
