tupla = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco',
         'seis', 'sete', 'oito', 'nove', 'dez',
         'onze', 'doze', 'trêze', 'catorze', 'quinze',
         'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    while True:
        numero = int(input('\nDigite um número entre [0..20]: '))
        if 0 <= numero <= 20:
            break
        else:
            print('Tente novamente...')
    print(f'Você digitou {tupla[numero]}. Até breve!')
    while True:
        resp = str(input('Quer digitar um número novamente? [S/N] ')).strip().upper()
        if resp in 'SsNs':
            break
    if resp == 'N':
        break
