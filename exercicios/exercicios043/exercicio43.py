peso = float(input('Digite o seu peso: '))
altura = float(input('Digite a sua altura: '))
imc = peso / (altura * altura)
if imc < 18.5:
    print('O IMC é de {:.2f} e você está ABAIXO DO PESO!'.format(imc))
elif imc < 25:
    print('O IMC é de {:.2f} e você está com o PESO IDEAL!'.format(imc))
elif imc < 30:
    print('O IMC é de {:.2f} e você está com SOBREPESO'.format(imc))
elif imc < 40:
    print('O IMC é de {:.2f} e você está com OBESIDADE'.format(imc))
else:
    print('O IMC é de {:.2f} e você está com OBESIDADE MÓRBIDA!!'.format(imc))
