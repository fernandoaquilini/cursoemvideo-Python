numero = soma = contador = 0
while True:
    numero = int(input('Digite um número inteiro (99 para parar!): '))
    if numero == 999:
        break
    else:
        soma += numero
        contador += 1
print(f'A soma dos {contador} números digitados foi {soma}!')
