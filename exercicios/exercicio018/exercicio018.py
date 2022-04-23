from math import sin, cos, tan, radians
angulo = float(input('Entre com o Valor do Ângulo X: '))
print('O Valor do Seno do Ângulo {}º é {}.'.format(angulo, sin(radians(angulo))))
print('O Valor do Cosseno do Ângulo {}º é {}.'.format(angulo, cos(radians(angulo))))
print('O Valor da Tangente do Ângulo {}º é {}.'.format(angulo, tan(radians(angulo))))
