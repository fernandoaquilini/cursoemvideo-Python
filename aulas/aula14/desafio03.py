opcao = 0
while opcao != 5:
    num01 = int(input('Digite o primeiro número: '))
    num02 = int(input('Digite o segundo número: '))
    print('[1] - SOMAR\n[2] - MULTIPLICAR\n[3] - MAIOR\n[4] - NOVOS NÚMEROS\n[5] - SAIR')
    opcao = int(input('Digite a opção desejada: '))
    if opcao == 1:
        print('A soma de {} e {} é {}!'.format(num01, num02, num01 + num02))
    elif opcao == 2:
        print('A multiplicação de {} e {} é {}!'.format(num01, num02, num01 * num02))
    elif opcao == 3:
        if num01 > num02:
            print('{} é maior que {}!'.format(num01, num02))
        elif num02 > num01:
            print('{} é maior que {}!'.format(num02, num01))
        else:
            print('{} e {} são iguais!'.format(num01, num02))
    elif opcao == 4:
        print('OK! Novos números...')
    elif opcao == 5:
        print('OK! Até breve!!')
    else:
        print('Opção Inválida! Vamos tentar novamente...')
