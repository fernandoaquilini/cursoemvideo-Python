num01 = int(input('Digite o primeiro valor: '))
num02 = int(input('Digite o segundo valor: '))
if num01 > num02:
    print('O primeiro valor {} é maior que o segundo valor {}!'.format(num01, num02))
elif num02 > num01:
    print('O primeiro valor {} é menor que o segundo valor {}!'.format(num01, num02))
else:
    print('O primeiro valor {} é igual ao segundo valor {}!'.format(num01, num02))
