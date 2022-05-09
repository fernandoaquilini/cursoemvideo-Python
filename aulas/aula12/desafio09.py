preco = float(input('Digite o valor normal do produto (R$): '))
print('1 - À Vista (Dinheiro/Cheque)')
print('2 - À Vista (Cartão)')
print('3 - 2x (Cartão)')
print('4 - 3x ou Mais (Cartão)')
opcao = int(input('Selecione a forma de pagamento: '))
if opcao == 1:
    print('Opção de pagamento 01 - À Vista (Dinheiro/Cheque)')
    print('Valor do produto: R$ {:.2f}'.format(preco - (preco * 10 / 100)))
elif opcao == 2:
    print('Opção de pagamento 02 - À Vista (Cartão)')
    print('Valor do produto: R$ {:.2f}'.format(preco - (preco * 5 / 100)))
elif opcao == 3:
    print('Opção de pagamento 03 - 2x (Cartão)')
    print('Valor do produto: R$ {:.2f}'.format(preco))
elif opcao == 4:
    print('Opção de pagamento 04 - 3x ou Mais (Cartão)')
    print('Valor do produto: R$ {:.2f}'.format(preco + (preco * 20 / 100)))
else:
    print('Opção de pagamento INVÁLIDA!')
