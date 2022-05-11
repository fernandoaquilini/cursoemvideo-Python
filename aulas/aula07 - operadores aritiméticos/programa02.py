# potência
print(pow(4, 3))
# raíz quadrada e raíz cúbica
print(81**(1/2))
print(125**(1/3))
# Operação com caracteres
print('Oi!'*3)
print('='*20)

# Operações com a formatação
nome = input('Qual o seu nome? ')
print('Seja bem vindo {:20}!'.format(nome))
print('Seja bem vindo {:>20}!'.format(nome))
print('Seja bem vindo {:<20}!'.format(nome))
print('Seja bem vindo {:^20}!'.format(nome))
print('Seja bem vindo {:=^20}!'.format(nome))
print('Seja bem vindo {}!'.format(nome))

# Operações com a formatação
nome = input('Qual o seu nome? ')
print('Não formatado {:20}!'.format(nome), end=' e ')
print('Right Align {:>20}!'.format(nome), end=' >>> ')
print('Left Align {:<20}!'.format(nome))
print('Center Align {:^20}!'.format(nome))
print('Preenchido {:=^20}!'.format(nome))
print('Quebrado \n{}!'.format(nome))
