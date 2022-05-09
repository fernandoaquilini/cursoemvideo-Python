largura = float(input('Entre com o valor da Largura da parede: '))
altura = float(input('Entre com o valor da Altura da parede: '))
area = largura * altura
print('Para esta parede de {:.2f}m², você vai precisar de {:.2f} latas de tinta de 1 litro cada.'.format(area, area/2))
