from random import randint

tupla = (randint(1, 100), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))

print(tupla)

maior = menor = 0
for cont in range(0, len(tupla)):
    if cont == 0:
        maior = menor = tupla[cont]
    else:
        if menor > tupla[cont]:
            menor = tupla[cont]
        if maior < tupla[cont]:
            maior = tupla[cont]
print(f'Maior número: {maior}. Menor número: {menor}.')
