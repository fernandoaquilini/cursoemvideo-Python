from lib.interface import *
from lib.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'

if not verifArquivo(arq):
    criarArquivo(arq)

while True:
    resp = menu(['Listar Cadastrados', 'Cadastrar Novo', 'Sair do Sistema'])
    if resp == 1:
        lerArquivo(arq)
    elif resp == 2:
        cabecalho('NOVO CADASTRO', 50)
        nome = str(input('Nome: ')).strip()
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resp == 3:
        cabecalho('Saindo do Sistema... Até breve!', 50)
        break
    else:
        print(f'\033[0;31mERRO! Opção Inválida.\033[m')
    sleep(2)
