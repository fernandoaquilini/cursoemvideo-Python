topo = ' Tabuada 3.0 '
print(f'{topo:-^30}')
while True:
    tabuada = int(input('\nDigite a tabuada escolhida (Número negativo para sair!): '))
    if tabuada < 0:
        break
    print(f'\nTabuada do {tabuada}!')
    for mult in range(1, 10+1):
        print(f'{tabuada} x {mult} = {tabuada * mult}!')
print('Obrigado, volte sempre!')
