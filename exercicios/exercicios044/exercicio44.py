preço = float(input('Digite o valor normal do produto (R$): '))
print('''
1 - À Vista (Dinheiro/Cheque)')
2 - À Vista (Cartão)
3 - 2x (Cartão)
4 - 3x ou Mais (Cartão)
''')
opção = int(input('Selecione a forma de pagamento: '))
if opção == 1:
    print('Opção de pagamento 01 - À Vista (Dinheiro/Cheque)')
    print('Valor do produto: R$ {:.2f}'.format(preço - (preço * 10 / 100)))
elif opção == 2:
    print('Opção de pagamento 02 - À Vista (Cartão)')
    print('Valor do produto: R$ {:.2f}'.format(preço - (preço * 5 / 100)))
elif opção == 3:
    print('Opção de pagamento 03 - 2x (Cartão)')
    print('Valor do produto: R$ {:.2f}'.format(preço))
    print('Valor das parcelas: R$ {:.2f}'.format(preço / 2))
elif opção == 4:
    parcelas = int(input('Quantas parcelas? '))
    print('Opção de pagamento 04 - 3x ou Mais (Cartão)')
    print('Valor do produto: R$ {:.2f}'.format(preço + (preço * 20 / 100)))
    print('Valor das parcelas: R$ {:.2f}'.format((preço + (preço * 20 / 100)) / parcelas))
else:
    print('Opção de pagamento INVÁLIDA!')
