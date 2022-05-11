nota01 = float(input('Digite a primeira nota: '))
nota02 = float(input('Digite a segunda nota: '))
media = (nota01 + nota02) / 2
if media < 5:
    status = 'REPROVADO!'
elif media < 6.9:
    status = 'EM RECUPERAÇÃO!'
else:
    status = 'APROVADO!'
print('A média foi {:.2f} e o aluno está {}!'.format(media, status))
