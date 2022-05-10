from functions import moeda, dados

valor = dados.leiaDinheiro('Digite um valor (R$): ')
moeda.resumo(valor, 20, 18)
