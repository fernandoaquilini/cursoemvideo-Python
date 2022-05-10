# import funções
# from funções import fatorial, dobro, triplo
from uteis import numeros

num = int(input("Digite o Valor: "))
print(f'O Fatorial de {num} é {numeros.fatorial(num)}.')
print(f'O Dobro de {num} é {numeros.dobro(num)}.')
print(f'O Triplo de {num} é {numeros.triplo(num)}.')
