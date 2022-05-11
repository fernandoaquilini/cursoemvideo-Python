primeiro = int(input('Digite o Primeiro Termo da PA: '))
razao = int(input('Digite a Razão da PA: '))
cont = 1
while cont <= 10:
    print('{} -> '.format(primeiro), end='')
    primeiro += razao
    cont += 1
print('FIM!')
novos = int(input('Gostaria de ver mais quantos Termos? '))
while novos != 0:
    cont = 1
    while cont <= novos:
        print('{} -> '.format(primeiro), end='')
        primeiro += razao
        cont += 1
    print('FIM!')
    novos = int(input('Gostaria de ver mais quantos Termos? '))
print('Agora é o FIM!')