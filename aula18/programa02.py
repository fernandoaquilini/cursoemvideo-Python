teste = []
teste.append('Fernando')
teste.append(45)

galera = list()
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 19
galera.append(teste[:])
print(galera)

galeraNova = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
print(galeraNova)
print(galeraNova[0])
print(galeraNova[0][0])
print(galeraNova[0][1])

for pessoa in galeraNova:
    print(f'{pessoa[0]} tem {pessoa[1]} anos!')

dado = []
amigos = []
for cont in range(0, 3):
    dado.append(str(input('Digite o nome: ')).strip().title())
    dado.append(int(input('Digite a idade: ')))
    amigos.append(dado[:])
    dado.clear()
print(amigos)

totmais = totmenos = 0
for p in amigos:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade')
        totmais += 1
    else:
        print(f'{p[0]} é menor de idade')
        totmenos += 1

print(f'Temos {totmais} maior(es) de idade e {totmenos} menor(es) de idade.')
