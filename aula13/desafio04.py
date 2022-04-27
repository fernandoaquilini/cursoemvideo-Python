num = int(input('Digite um número inteiro qualquer: '))
print('A tabuada do {} é:'.format(num))
print('-' * 15)
for cont in range(1, 10+1):
    print('{} X {:>2} = {}'.format(num, cont, num*cont))
print('-' * 15)
