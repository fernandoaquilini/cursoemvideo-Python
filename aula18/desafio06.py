notas = []
aluno = []
classe = []
while True:
    aluno.append(str(input('Digite o nome do aluno: ')).strip().title())
    notas.append(float(input('Digite a primeira nota: ')))
    notas.append(float(input('Digite a segunda nota: ')))
    aluno.append(notas[:])
    notas.clear()
    classe.append(aluno[:])
    aluno.clear()
    opcao = str(input('Deseja continuar? [S/N]: ')).strip().upper()
    if opcao in 'N':
        break
# print(classe)
print('-=' * 30)
print(f'{"No.":<5}{"NOME":<30}{"MÉDIA":<5}')
print('-' * 40)
for l, a in enumerate(classe):
    print(f'{l:<5}{a[0].title():<30}{(a[1][0]+a[1][1])/2:>5.2f}')
while True:
    print('-' * 40)
    indice = int(input('Mostrar as notas de qual aluno? (999 interrompe): '))
    if indice != 999:
        print(f'As notas do {classe[indice][0]} foram {classe[indice][1]}')
    else:
        break
