total = 0
produtosMil = 0
maisbaratoV = 0
maisbaratoN = ''
maisbaratoF = True
while True:
    nome = str(input('\nDigite o nome do Produto: '))
    qtde = int(input('Digite a quantidade do Produto: '))
    valor = float(input('Digite o valor unitário do Produto: '))
    if maisbaratoF:
        maisbaratoN = nome
        maisbaratoV = valor
        maisbaratoF = False
    else:
        if maisbaratoV > valor:
            maisbaratoN = nome
            maisbaratoV = valor
    if valor > 1000:
        produtosMil += qtde
    total += qtde * valor
    while True:
        saida = str(input('Deseja lançar novo produto? [S/N]: ')).strip().upper()[0]
        if saida in 'SN':
            break
    if saida == 'N':
        break
print('-'*40)
print(f'O valor total da compra foi de R$ {total:.2f}.')
print(f'Foram {produtosMil} produto(s) comprado(s) acima de R$ 1000,00.')
print(f'E o produto mais barato foi {maisbaratoN}, no valor de R$ {maisbaratoV:.2f}')
