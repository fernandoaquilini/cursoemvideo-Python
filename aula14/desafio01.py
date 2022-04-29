sexo = ''
while sexo[:1] != 'M' and sexo[:1] != 'F':
    sexo = str(input('Digite o seu SEXO [M/F]: ')).strip().upper()
print('Valor OK!')
