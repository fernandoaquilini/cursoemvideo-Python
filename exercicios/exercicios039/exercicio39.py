from datetime import date
atual = date.today().year
nascimento = int(input('Digite o ano do seu nascimento: '))
idade = atual - nascimento
print('Quem nasceu em {} tem {} ano(s) em {}!'.format(nascimento, idade, atual))
if idade < 18:
    print('Você ainda terá que se alistar!')
    print('Faltam {} ano(s)! Será no ano de {}!'.format(18 - idade, atual + (18 - idade)))
elif idade == 18:
    print('Você deve se alistar este ano!')
else:
    print('Passou do tempo de se alistar!')
    print('Já se passaram {} ano(s)! Deveria ter se alistado em {}!'.format(idade - 18, atual - (idade - 18)))
