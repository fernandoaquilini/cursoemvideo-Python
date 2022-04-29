maiorpeso = 0
menorpeso = 0
for cont in range(1, 5+1):
    peso = float(input('Digite o peso da {}ª pessoa: '.format(cont)))
    if cont == 1:
        maiorpeso = peso
        menorpeso = peso
    else:
        if peso > maiorpeso:
            maiorpeso = peso
        if peso < menorpeso:
            menorpeso = peso
print('Maior peso: {:.2f}'.format(maiorpeso))
print('Menor peso: {:.2f}'.format(menorpeso))
