nome = str(input('Digite seu nome completo, por gentileza: ')).strip()
lista = nome.split()
print('Nome completo: {}\nPrimeiro nome: {}\nÚltimo nome: {}'.format(nome, lista[0], lista[len(lista)-1]))
