lado1 = float(input('Digite o lado 01: '))
lado2 = float(input('Digite o lado 02: '))
lado3 = float(input('Digite o lado 03: '))
if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2:
    print('Os segmentos FORMAM um triângulo!')
else:
    print('Os segmentos NÃO FORMAM um triângulo!')
