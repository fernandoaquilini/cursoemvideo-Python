linha = []
matriz = []
somapares = somaterceira = maiorvalor = 0
for l in range(0, 3):
    for c in range(0, 3):
        valor = int(input(f'Digite o calor da casa {l+1}x{c+1} = '))
        linha.append(valor)
        if valor % 2 == 0:
            somapares += valor
        if c == 2:
            somaterceira += valor
        if l == 1 and valor > maiorvalor:
            maiorvalor = valor
    matriz.append(linha[:])
    linha.clear()

for l in matriz:
    print(f'[{l[0]:^5}] [{l[1]:^5}] [{l[2]:^5}]')

print(f'A soma de todos os valores pares foi {somapares}.')
print(f'A soma de todos os valores da terceira coluna foi {somaterceira}.')
print(f'O maior valor da segunda linha foi {maiorvalor}.')
# print(matriz)
