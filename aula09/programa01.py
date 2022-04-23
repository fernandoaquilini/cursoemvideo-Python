frase = 'Curso em Vídeo Python'

#Fatiamento
print(frase[9])
print(frase[9:13])
print(frase[9:21])
print(frase[9:len(frase)])
print(frase[9:21:2])
print(frase[::2])
print(frase[:5])
print(frase[15:])
print(frase[9::3])

#Análise
print(len(frase))
print(frase.count('o'))
print(frase.count('o', 0, 13))
print(frase.count('o', 0, 14))
print(frase.find('deo'))
print(frase.find('Android'))
print('Curso' in frase)

#Transformação
print(frase.replace('Python', 'Android'))
print(frase)
print(frase.upper())
print(frase.lower())
print(frase.capitalize())
print(frase.title())

#Divisão de String
print(frase.split())
dividido = frase.split()
print(dividido[1])
print(dividido[2][0])
print(frase.title().split())

#Junção de String
print('-'.join(frase.split()))
print('-'.join(frase.lower().split()))

#Alterando em definitivo
frase = frase.replace('Python', 'Android')
print(frase)

#Correção de Texto
novafrase = '   Aprenda Python  '
print(novafrase)
print(novafrase.strip())
print(novafrase.rstrip())
print(novafrase.lstrip())

print("""Lorem ipsum dolor sit amet, consectetur adipiscing elit.
Morbi varius risus faucibus feugiat tincidunt.
Duis nibh lectus, tempor in tortor ut, rhoncus facilisis erat.
Etiam molestie blandit lacinia. Integer in augue diam.
Nam quis euismod lacus. Sed accumsan eleifend arcu eget feugiat.
Fusce semper mollis dui vel auctor.""")



