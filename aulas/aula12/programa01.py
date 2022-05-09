nome = str(input('Digite seu nome: '))
if nome == 'Fernando':
    print('Que nome Lindo!')
elif nome == 'Maria' or nome == 'João':
    print('Que nome Popular!')
elif nome in 'Creuza Diornes Ednalva':
    print('Que nome Estranho!')
else:
    print('Que nome Normal!')
print('Tenha um bom dia, {}'.format(nome))
