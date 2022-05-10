salario = float(input('Entre o valor do salário atual do funcionário: R$ '))
print('Com 15% de aumento, o novo salário do funcionário será R$ {:.2f}.'.format(salario * 1.15))

print('Com 15% de aumento, o novo salário do funcionário será R$ {:.2f}.'.format(salario + ((salario * 15)/100)))
