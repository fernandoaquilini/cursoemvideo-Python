soma = cont = maior = menor = 0
executa = 'S'
while executa not in 'Nn':
    valor = int(input('Digite um número: '))
    if cont == 1:
        maior = menor = valor
    else:
        if valor > maior:
            maior = valor
        if valor < menor:
            menor = valor
    cont += 1
    soma += valor
    executa = str(input('Gostaria de digitar outro número: [S/N]? ')).strip().upper()[0]
print('A soma dos {} digitados foi {}!'.format(cont, soma))
print('A média dos {} digitados foi {}!'.format(cont, soma / cont))
print('O maior número foi {}!'.format(maior))
print('O menor número foi {}!'.format(menor))

