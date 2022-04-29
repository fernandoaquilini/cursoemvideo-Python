fatorial = 1
numero = int(input('Digite um número: '))
for cont in range(fatorial, numero+1):
    fatorial *= cont
print('{}! é igual a {}!'.format(numero, fatorial))

contador = 1
fatorial = 1
numero = int(input('Digite um número: '))
while contador <= numero:
    fatorial *= contador
    contador += 1
print('{}! é igual a {}!'.format(numero, fatorial))
