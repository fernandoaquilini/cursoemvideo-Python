numero = str(input('Digite um valor entre 0 e 9999: '))
if len(numero) == 4:
    print('Unidade: {}'.format(numero[3]))
    print('Dezena: {}'.format(numero[2]))
    print('Centena: {}'.format(numero[1]))
    print('Milhar: {}'.format(numero[0]))
elif len(numero) == 3:
    print('Unidade: {}'.format(numero[2]))
    print('Dezena: {}'.format(numero[1]))
    print('Centena: {}'.format(numero[0]))
elif len(numero) == 2:
    print('Unidade: {}'.format(numero[1]))
    print('Dezena: {}'.format(numero[0]))
elif len(numero) == 1:
    print('Unidade: {}'.format(numero[0]))
else:
    print('Você não digitou corretamente!')
