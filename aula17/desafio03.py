lista = []
for cont in range(0, 5):
    valor = int(input('Digite um valor: '))
    if len(lista) == 0:
        lista.append(valor)
        print('Adicionado ao final da lista')
    else:
        pos = 0
        while pos <= len(lista):
            if pos == len(lista):
                lista.append(valor)
                print('Adicionado ao final da lista')
                break
            else:
                if lista[pos] < valor:
                    pos += 1
                else:
                    lista.insert(pos, valor)
                    print(f'Adicionado na posição {pos}!')
                    break
print(lista)
