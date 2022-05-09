valor = int(input('Digite in valor: '))
print('Valor digitado: ', valor)
print(type(valor))

valor = str(input('Digite in valor: '))
print('Valor digitado: ', valor)
print(type(valor))

valor = float(input('Digite in valor: '))
print('Valor digitado: ', valor)
print(type(valor))

valor = bool(input('Digite in valor: '))
print('Valor digitado: ', valor)
print(type(valor))

valor = input('Digite algo: ')
print(valor.isnumeric())

valor = input('Digite in algo: ')
print(valor.isalfa())
print(valor.isalnum())
print(valor.isupper())
print(valor.islower())
