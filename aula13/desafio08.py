frase = str(input('Digite uma frase: '))
check01 = ''
for cont in range(0, len(frase)):
    if frase[cont] != ' ':
        check01 = check01 + frase[cont]
print(check01)
check02 = ''
for cont in range(len(frase)-1, -1, -1):
    if frase[cont] != ' ':
        check02 = check02 + frase[cont]
print(check02)
if check01 == check02:
    print('A frase é Palíndromo!!')
else:
    print('A frase é não é Palíndromo!!')
