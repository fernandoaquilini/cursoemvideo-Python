aluno = dict()
aluno['nome'] = str(input('Digite o nome do aluno(a): ')).strip().title()
aluno['média'] = float(input(f'Digite a média de {aluno["nome"]}: '))
if aluno['média'] >= 6:
    aluno['status'] = 'Aprovado'
else:
    aluno['status'] = 'Reprovado'
for k, v in aluno.items():
    print(f'{k.capitalize()} é igual a {v}')
