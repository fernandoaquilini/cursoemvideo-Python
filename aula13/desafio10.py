maiorpeso = 0
menorpeso = 9999
for cont in range(1, 5+1):
    peso = float(input('Digite o peso da {}ª pessoa: '.format(cont)))
    if peso > maiorpeso:
        maiorpeso = peso
    if peso < menorpeso:
        menorpeso = peso
print('Maior peso: {:.2f}'.format(maiorpeso))
print('Menor peso: {:.2f}'.format(menorpeso))
