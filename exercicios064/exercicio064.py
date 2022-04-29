soma = cont = 0
flag = True
valor = int(input('Digite um número: '))
while valor != 999:
    cont += 1
    soma += valor
    valor = int(input('Digite um número: '))
print('A soma dos {} digitados foi {}!'.format(cont, soma))
