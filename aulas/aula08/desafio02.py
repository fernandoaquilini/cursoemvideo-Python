from math import sqrt
catopo = float(input('Digite o valor do Cateto Oposto: '))
catadj = float(input('Digite o valor do Cateto Adjacente: '))
hipo = sqrt(catadj * catadj + catopo * catopo)
print('A Hipotenusa para os Catetos digitados é {}!'.format(hipo))
