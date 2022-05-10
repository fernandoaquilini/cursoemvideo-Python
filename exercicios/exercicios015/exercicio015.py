dias = int(input('Quantos dias o carro ficou alugado? '))
kms = float(input('Quantos Kms rodou ao total? '))
print('O valor total a pagar é R$ {:.2f}.'.format((dias * 60)+(kms * 0.15)))
