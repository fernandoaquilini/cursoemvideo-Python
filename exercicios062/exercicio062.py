primeiro = int(input('Digite o Primeiro Termo da PA: '))
razao = int(input('Digite a Razão da PA: '))
cont = 1
while cont <= 10:
    print('{} -> '.format(primeiro), end='')
    primeiro += razao
    cont += 1
print('FIM!')
total = 10
flag = True
while flag:
    novos = int(input('Gostaria de ver mais Termos? Digite a Quantidade ou [ 0 ] para sair! '))
    total += novos
    if novos == 0:
        flag = False
    else:
        cont = 1
        while cont <= novos:
            print('{} -> '.format(primeiro), end='')
            primeiro += razao
            cont += 1
        print('FIM!')
print('Agora é o FIM! Foram exibidos {} Termos!'.format(total))

