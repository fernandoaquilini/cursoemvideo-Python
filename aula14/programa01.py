for c in range(1, 10):
    print(c)
print('FIM!')

contador = 1
while contador < 10:
    print(contador)
    contador += 1
print('FIM!')

valor = 1
while valor != 0:
    valor = int(input('Digite um valor inteiro: [0 - SAIR] '))

resposta = 'S'
soma = 0
while resposta[:1] == 'S':
    número = int(input('Digite um valor: '))
    resposta = str(input('Quer Continuar? [S/N] ')).strip().upper()
    soma += número
print(soma)

n = 1
pares = ímpares = 0
while n != 0:
    n = int(input('Digite um número: '))
    if n != 0:
        if n % 2 == 0:
            pares +=1
        else:
            ímpares += 1
print('Você digitou {} pares e {} ímpares!'.format(pares, ímpares))
