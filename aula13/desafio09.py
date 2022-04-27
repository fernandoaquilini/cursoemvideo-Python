from datetime import date
anoatual = date.today().year
contmaiores = 0
contmenores = 0
for cont in range(1, 7+1):
    ano = int(input('Digite o ano de nascimento da {}ª pessoa: '.format(cont)))
    idade = anoatual - ano
    if idade >= 21:
        contmaiores = contmaiores + 1
    else:
        contmenores = contmenores + 1
print('Maiores de idade: {}.'.format(contmaiores))
print('Menores de idade: {}.'.format(contmenores))
