frase = str(input('Digite a sua frase inteira: '))
print('Na frase aparecem {} letras A em maíusculo e {} letra a em minúsculo!'.format(frase.count('A'), frase.count('a')))
print('A primeira ocorrência é na posição {}...'.format(frase.strip().find('a')))
print('A última ocorrência é na posição {}...'.format(frase.strip().rfind('a')))
