soma = 0
for cont in range(1, 500+1):
    if cont % 2 == 1 and cont % 3 == 0:
        soma += cont
print('A soma de todos os números ímpares entre 1 e 500 é \033[31m{}'.format(soma))
