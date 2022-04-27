somaidade = 0
contaidade = 0
temhomem = False
homemvelhoidade = 0
homemvelhonome = ''
contmulheres = 0
for cont in range(1, 4+1):
    nome = str(input('Digite o nome da {}ª pessoa: '.format(cont))).strip()
    idade = int(input('Digite a idade da {}ª pessoa: '.format(cont)))
    somaidade = somaidade + idade
    contaidade = contaidade + 1
    sexo = str(input('Digite o sexo da {}ª pessoa: [M/F]: '.format(cont))).strip().upper()
    if sexo[:1] == 'M':
        temhomem = True
        if idade > homemvelhoidade:
            homemvelhoidade = idade
            homemvelhonome = nome
    elif sexo[:1] == 'F' and idade <= 21:
        contmulheres = contmulheres + 1
print('A média de idade do grupo é de {:.2f} anos!'.format(somaidade / contaidade))
if temhomem:
    print('O homem mais velhor do grupo é o {} que está com {} ano(S)!'.format(homemvelhonome, homemvelhoidade))
else:
    print('Não identificamos homens no grupo!')
print('E no grupo, existem {} mulher(es) abaixo da maioridade!'.format(contmulheres))
