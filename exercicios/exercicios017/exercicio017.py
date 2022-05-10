from math import sqrt, hypot
catopo = float(input('Digite o valor do Cateto Oposto: '))
catadj = float(input('Digite o valor do Cateto Adjacente: '))
#hipo = sqrt(catadj * catadj + catopo * catopo)
hipo = hypot(catopo, catadj)
print('A Hipotenusa para os Catetos digitados é {}!'.format(hipo))
