sexo = ' '
while sexo not in 'MmFf':
    sexo = str(input('Digite o seu SEXO [M/F]: ')).strip().upper()[0]
print('Valor {} registrado com sucesso!'.format(sexo))
