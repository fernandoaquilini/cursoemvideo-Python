tempo = int(input('Quanto tempo tem seu carro: '))
print('---INICIO---')
if tempo <= 3:
    print('Carro Novo!')
else:
    print('Carro Velho!')
print('---FIM---')

print('Carro Novo!' if tempo <= 3 else 'Carro Velho!')
