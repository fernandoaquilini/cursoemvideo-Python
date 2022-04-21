# Ordem de Precedência
# 01 - ()
# 02 - **
# 03 - * / // %
# 04 - + -
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
print('A soma entre {} e {} é igual a {}'.format(n1, n2, n1 + n2))
print('A subtração entre {} e {} é igual a {}'.format(n1, n2, n1 - n2))
print('A multiplicação entre {} e {} é igual a {}'.format(n1, n2, n1 * n2))
print('A divisão entre {} e {} é igual a {:.5f}'.format(n1, n2, n1 / n2))
print('A exponenciação entre {} e {} é igual a {}'.format(n1, n2, n1 ** n2))
print('A divisão de inteiros entre {} e {} é igual a {}'.format(n1, n2, n1 // n2))
print('O resto da divisão entre {} e {} é igual a {}'.format(n1, n2, n1 % n2))
