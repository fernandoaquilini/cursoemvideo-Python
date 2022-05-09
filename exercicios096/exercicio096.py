def area(larg, comp):
    area = larg * comp
    return area


print('Controle de Terrenos')
print('-' * 20)
larg = float(input('LARGURA (m): '))
comp = float(input('COMPRIMENTO (m): '))
print(f'A área do terreno de {larg:.2f} x {comp:.2f} é de {area(larg, comp):.2f}m².')
