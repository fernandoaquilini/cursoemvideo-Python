from datetime import date
nascimento = int(input('Digite o ano do seu nascimento: '))
atual = date.today().year
if atual - nascimento < 18:
    print('Você ainda terá que se alistar!')
    print('Faltam {} ano(s)!'.format(18 - (atual - nascimento)))
elif atual - nascimento == 18:
    print('Você deve se alistar este ano!')
else:
    print('Passou do tempo de se alistar!')
    print('Já se passaram {} ano(s)'.format((atual - nascimento) - 18))
print('Você está com {} anos!'.format(atual - nascimento))
