velocidade = float(input('Qual velocidade estava o carro: '))
if velocidade > 80:
    print('Você foi MULTADO! Sua multa será no valor de R$ {:.2f}.'.format((velocidade-80)*7))
else:
    print('Velocidade aceita!')
