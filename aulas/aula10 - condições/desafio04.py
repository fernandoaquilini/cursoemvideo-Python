distância = float(input('Qual a distância da viagem em Km? '))
if distância <= 200:
    print('A sua passagem custa R$ {:.2f}'.format(distância * 0.5))
else:
    print('A sua passagem custa R$ {:.2f}'.format(distância * 0.45))
