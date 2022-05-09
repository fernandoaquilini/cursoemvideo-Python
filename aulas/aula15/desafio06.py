cedA = cedB = cedC = cedD = 0
valorSaque = int(input('\nDigite o valor do saque [R$]: '))
if valorSaque // 50 > 0:
    cedA = valorSaque // 50
    valorSaque -= cedA * 50
    print(f'Total de {cedA} cédulas de R$ 50.00')
if valorSaque // 20 > 0:
    cedB = valorSaque // 20
    valorSaque -= cedB * 20
    print(f'Total de {cedB} cédulas de R$ 20.00')
if valorSaque // 10 > 0:
    cedC = valorSaque // 10
    valorSaque -= cedC * 10
    print(f'Total de {cedC} cédulas de R$ 10.00')
if valorSaque // 1 > 0:
    cedD = valorSaque // 1
    valorSaque -= cedD * 1
    print(f'Total de {cedC} cédulas de R$ 1.00')
