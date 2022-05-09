# escopo de variáveis
def teste():
    global n
    n = 8
    x = 8
    print(f'Na Função Teste, n vale {n}.')
    print(f'Na Função Teste, x vale {x}.')

# retorno de resultados


# Main
n = 2
teste()
print(f'No Programa principal, n vale {n}.')
