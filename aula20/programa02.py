def soma(a, b):
    soma = a + b
    return soma


def contador(* núm):
    print(f'Foram {len(núm)} parâmetros! São eles: {núm}.')


def dobra(lista):
    for i in range(0, len(lista)):
        lista[i] = lista[i] * 2


print(f'A soma é igual a {soma(6, 7)}.')
print(f'A soma é igual a {soma(a=96, b=87)}.')
print(f'A soma é igual a {soma(b=76, a=67)}.')

# empacotadore de parâmetros
contador(1, 4, 7, 0)
contador(2, 5, 8)
contador(3, 6, 9, 10, 11)

valores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
dobra(valores)
print(valores)
