soma = 0
cont = 0
flag = True
while flag:
    valor = int(input('Digite um número: '))
    if valor == 999:
        flag = False
    else:
        cont += 1
        soma += valor
print('A soma dos {} digitados foi {}!'.format(cont, soma))

