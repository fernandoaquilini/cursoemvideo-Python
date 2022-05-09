lista = []
for cont in range(0, 5):
    lista.append(int(input(f'Digite um valor para a posição {cont}: ')))
print('-=' * 30)
print(f'Você digitou os valores {lista}')
maior = max(lista)
print(f'O maior valor digitado foi {maior} nas posições ', end='')
for p in range(0, len(lista)):
    if lista[p] == maior:
        print(f'{p}... ', end='')
menor = min(lista)
print(f'\nO menor valor digitado foi {menor} nas posições ', end='')
for p in range(0, len(lista)):
    if lista[p] == menor:
        print(f'{p}... ', end='')
