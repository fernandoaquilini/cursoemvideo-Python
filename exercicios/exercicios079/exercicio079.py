lista = []
opcao = 'S'
while True:
    valor = int(input('Digite um valor: '))
    if valor not in lista:
        lista.append(valor)
        print('Valor adicionado com sucesso!')
    else:
        print(f'O valor {valor} já existe na lista! Não foi adicionado.')
    opcao = str(input('Quer continuar? [S/N]: ')).strip().upper()
    if opcao in 'N':
        break
lista.sort()
print(f'Você inseriu os seguintes valores: {lista}!')
