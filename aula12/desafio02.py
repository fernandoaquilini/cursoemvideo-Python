número = int(input('Digite um número inteiro qualquer: '))
print('Selecione a base para conversão:')
print('1 - Binário')
print('2 - Octal')
print('3 - Hexadecimanal')
opção = int(input('Digite a sua opção: '))
if opção == 1:
    print('Resultado: {}!'.format(bin(número)))
elif opção == 2:
    print('Resultado: {}!'.format(oct(número)))
elif opção == 3:
    print('Resultado: {}!'.format(hex(número)))
else:
    print('Opção inválida!')
