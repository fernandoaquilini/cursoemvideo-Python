tot18 = totM = totF20 = 0
while True:
    idade = int(input('\nDigite a Idade da pessoa: '))
    while True:
        sexo = str(input('Digite o Sexo da pessoa [M/F]: ')).strip().upper()[0]
        if sexo in 'MmFf':
            break
    if idade >= 18:
        tot18 += 1
    if sexo in 'M':
        totM += 1
    if sexo in 'F' and idade < 20:
        totF20 += 1
    while True:
        saida = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
        if saida in 'SsNn':
            break
    if saida in 'N':
        break
print(f'Você inseriu {tot18} pessoa(s) maiores de 18 anos!')
print(f'Você inseriu {totM} pessoa(s) do sexo masculino!')
print(f'Você inseriu {totF20} pessoa(s) do sexo feminino menores de 20 anos!')
