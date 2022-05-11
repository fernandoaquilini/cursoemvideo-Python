from random import randint

cont = 1
while cont <= 10:
    print(cont, '-> ', end='')
    cont += 1
print('FIM!')

val = 0
while True:
    val = randint(1, 9)
    # print(val, '-> ', end='')
    print(f'{val} -> ', end='')
    if val == 5:
        break
print('FIM!')

nome = 'Fernando'
idade = 45
valor = 10000
print(f'{nome}, de {idade} anos, recebe R$ {valor:.2f}')
print(f'{nome:-^20}, de {idade} anos, recebe R$ {valor:.2f}')
print(f'{nome:->20}, de {idade} anos, recebe R$ {valor:.2f}')
print(f'{nome:-<20}, de {idade} anos, recebe R$ {valor:.2f}')
