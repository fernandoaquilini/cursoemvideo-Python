lanche = ['Hamburger', 'Suco', 'Pizza', 'Pudim']
print(lanche)

# insere no último
print('Com inserção após o último elemento...')
lanche.append('Picolé')
print(lanche)

# insere na posição indicada
print('Insere no índice 0')
lanche.insert(0, 'HotDog')
print(lanche)

# altera o valor no índice
print('Altera o conteudo do índice específico')
lanche[2] = 'Refrigerante'
print(lanche)

# apaga no índice
print('Um método de apagar...')
del lanche[3]
print(lanche)
lanche.insert(3, 'Pizza')
print(lanche)
print('Outro método de apagar...')
lanche.pop(3)
print(lanche)
lanche.insert(3, 'Pizza')
print(lanche)

print('Apagando buscando o conteúdo...')
lanche.remove('Pizza')
print(lanche)
lanche.insert(3, 'Pizza')
print(lanche)

print('Apagando o último elemento...')
lanche.pop()
print(lanche)
lanche.append('Picolé')
print(lanche)

print('Apagando garantindo que não terá erro...')
if 'Pizza' in lanche:
    lanche.remove('Pizza')
    print(lanche)
    lanche.insert(3, 'Pizza')
    print(lanche)

valores = list(range(4, 11))
print(valores)

valores = list(range(1, 11, 2))
print(valores)

# ordenação de lista
valores = [8, 2, 5, 4, 9, 3, 0]
print(valores)
valores.sort()
print(valores)
# ordem reversa
valores.sort(reverse=True)
print(valores)

# tamanho da lista
print(len(valores))