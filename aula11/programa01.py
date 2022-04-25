'''
Style
0 - none
1 - bold
4 - underline
7 - negative

Color
30 - white
31 - red
32 - green
33 - yellow
34 - blue
35 - pink
36 - cian
37 - grey

Background
40 - white
41 - red
42 - green
43 - yellow
44 - blue
45 - pink
46 - cian
47 - grey

'''
print('\033[1;31mOlá, Mundo!')
print('\033[31mOlá, Mundo!\033[m')

print('\033[1;37mOlá, Mundo!\033[m')
print('\033[1;30;47mOlá, Mundo!\033[m')

nome = 'Fernando Ricardo Vito Aquilini'
print('Olá {}{}{}!!'.format('\033[1;36m', nome, '\033[m'))

cores = {
    'limpa':'\033[m',
    'vermelho':'\033[31m',
    'verde':'\033[32m',
    'amarelo':'\033[33m',
    'azul':'\033[34m',
    'rosa':'\033[35m',
    'pretoebranco':'\033[1;30;47m'
}
print('Olá {}{}{}!!'.format(cores['verde'], nome, cores['limpa']))
print('Olá {}{}{}!!'.format(cores['pretoebranco'], nome, cores['limpa']))
