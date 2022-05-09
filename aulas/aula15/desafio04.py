maiores = homens = menores = 0
while True:
    idade = int(input('\nDigite a Idade da pessoa: '))
    while True:
        sexo = str(input('Digite o Sexo da pessoa [M/F]: ')).strip().upper()[0]
        if sexo in 'MmFf':
            break
    while True:
        saida = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
        if saida in 'SsNn':
            break
    if idade > 18:
        maiores += 1
    if sexo in 'M':
        homens += 1
    if sexo in 'F' and idade < 20:
        menores += 1
    if saida in 'N':
        break
print(f'Você inseriu {maiores} pessoa(s) maiores de 18 anos!')
print(f'Você inseriu {homens} pessoa(s) do sexo masculino!')
print(f'Você inseriu {menores} pessoa(s) do sexo feminino menores de 20 anos!')
