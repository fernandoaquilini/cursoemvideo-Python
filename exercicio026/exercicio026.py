frase = str(input('Digite a sua frase inteira: ')).strip().upper()
print('Na frase aparecem {} letras A!'.format(frase.count('A')))
print('A primeira ocorrência é na posição {}...'.format(frase.find('A')+1))
print('A última ocorrência é na posição {}...'.format(frase.rfind('A')+1))
