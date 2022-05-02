linha = []
matriz = []
for l in range(0, 3):
    for c in range(0, 3):
        linha.append(int(input(f'Digite o calor da casa {l+1}x{c+1} = ')))
    matriz.append(linha[:])
    linha.clear()
for l in matriz:
    print(f'[{l[0]:^5}] [{l[1]:^5}] [{l[2]:^5}]')
