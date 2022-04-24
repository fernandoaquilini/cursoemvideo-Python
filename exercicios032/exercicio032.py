from datetime import date
ano = int(input('Digite o ano que você quer analisar: '))

if ano == 0:
    ano = date.today().year

print('Ano Bissexto básico!' if ano % 4 == 0 else 'Ano Não Bissexto básico!')

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('Ano Bissexto Top!')
else:
    print('Ano Não Bissexto Top!')
