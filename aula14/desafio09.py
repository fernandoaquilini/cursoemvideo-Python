soma = cont = maior = menor = 0
flag = True
flagfirst = False
while flag:
    valor = int(input('Digite um número: '))
    if not flagfirst:
        maior = valor
        menor = valor
        flagfirst = True
    else:
        if valor > maior:
            maior = valor
        if valor < menor:
            menor = valor
    cont += 1
    soma += valor
    saida = str(input('Gostaria de digitar outro número: [S/N]? ')).strip().upper()
    if saida[:1] == 'N':
        flag = False
print('A soma dos {} digitados foi {}!'.format(cont, soma))
print('A média dos {} digitados foi {}!'.format(cont, soma / cont))
print('O maior número foi {}!'.format(maior))
print('O menor número foi {}!'.format(menor))

