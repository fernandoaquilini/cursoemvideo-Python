tupla = ('Lápis', 1.75, 'Borracha', 2, 'Caderno', 15.9, 'Estojo', 25, 'Transferidor', 4.2,
         'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90, 'Dorgas', 532)

print('-' * 50)
print('{:^50}'.format('LISTAGEM DE PREÇOS'))
print('-' * 50)
for cont in range(0, len(tupla), 2):
    print(f'{tupla[cont]:.<40}R${tupla[cont+1]:>.2f}')
print('-' * 50)
