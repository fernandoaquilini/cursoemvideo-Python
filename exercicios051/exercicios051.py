primeiro = int(input('Digite o Primeiro Termo da PA: '))
razao = int(input('Digite a Razão da PA: '))
final = primeiro + (10 - 1) * razao
for cont in range(primeiro, final + razao, razao):
    print('{} -> '.format(cont), end='')
print('FIM!')