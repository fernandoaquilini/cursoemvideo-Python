from random import choice
aluno01 = str(input('Digite o nome do Aluno 01: '))
aluno02 = str(input('Digite o nome do Aluno 02: '))
aluno03 = str(input('Digite o nome do Aluno 03: '))
aluno04 = str(input('Digite o nome do Aluno 04: '))
escolhido = choice([aluno01, aluno02, aluno03, aluno04])
print('O aluno escolhido foi {}.'.format(escolhido))
