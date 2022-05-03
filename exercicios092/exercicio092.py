from datetime import date
trabalhador = dict()
trabalhador['nome'] = str(input('Digite no nome da pessoa: ')).strip().title()
nascimento = int(input('Digite o ano de nascimento: '))
hoje = date.today().year
trabalhador['idade'] = hoje - nascimento
trabalhador['ctps'] = str(input('Digite o número da carteira de trabalho: '))
if trabalhador['ctps'] != '0':
    trabalhador['contratação'] = int(input('Digite o ano da contratação: '))
    trabalhador['salário'] = float(input('Digite o salário (R$): '))
    trabalhou = hoje - trabalhador['contratação']
    trabalhador['aposentadoria'] = trabalhador['idade'] + (35 - trabalhou)
# print(trabalhador)
print('-=' * 10)
for k, v in trabalhador.items():
    print(f'No campo {k.capitalize()} temos o valor {v}.')
