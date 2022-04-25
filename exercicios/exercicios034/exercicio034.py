salário = float(input('Digite o valor do salário atual: '))
if salário > 1250:
    aumento = salário * 0.1
else:
    aumento = salário * 0.15
print('O aumento será de R$ {:.2f} e o salário passará para R$ {:.2f}.'.format(aumento, salário + aumento))
