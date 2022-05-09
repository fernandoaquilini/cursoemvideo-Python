nome = str(input("Digite o nome completo: "))
nome = nome.strip()
primeironome = nome[:nome.find(' ')]
print(nome.upper())
print(nome.lower())
print('O nome completo possui {} letras.'.format(len(nome)-nome.count(' ')))
print('O primeiro nome possui {} letras.'.format(len(primeironome)))
