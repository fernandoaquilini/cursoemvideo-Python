lista = []
while True:
    valor = int(input('Digite um valor: '))
    lista.append(valor)
    print('Valor adicionado com sucesso!')
    opcao = str(input('Quer continuar? [S/N]: ')).strip().upper()
    if opcao in 'N':
        break
print(f'Foram digitados {len(lista)} números.')
lista.sort(reverse=True)
print(f'A lista em ordem reversa: {lista}')
if 5 in lista:
    print('O Valor 5 foi digitado na lista!')
else:
    print('O Valor 5 não foi digitado na lista!')
