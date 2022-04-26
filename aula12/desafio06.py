from datetime import date
nascimento = int(input('Digite o ano de nascimento: '))
atual = date.today().year
if atual - nascimento <= 9:
    print('Nadador MIRIM!')
elif atual - nascimento <= 14:
    print('Nadador INFANTIL!')
elif atual - nascimento <= 19:
    print('Nadador JUNIOR!')
elif atual - nascimento <= 20:
    print('Nadador SÊNIOR!')
else:
    print('Nadador MASTER!')
print('Idade é {}.'.format(atual - nascimento))
