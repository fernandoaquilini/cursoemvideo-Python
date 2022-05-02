expressão = str(input('Digite a sua expressão: '))
pilha = []
for cont in expressão:
    if cont == '(':
        pilha.append(cont)
    elif cont == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
print(pilha)
if len(pilha) == 0:
    print('Expressão correta!!')
else:
    print('Expressão incorreta!!')
