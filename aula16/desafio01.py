tupla = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
         'onze', 'doze', 'trêze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    numero = int(input('\nDigite um número entre [0..20]: '))
    if numero >= 0 and numero <= 20:
        break
    else:
        print('Tente novamente...')
print(f'Você digitou {tupla[numero]}. Até breve!')
