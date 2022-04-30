tupla = ('aprender', 'programar', 'linguagem', 'python',
         'curso', 'gratis', 'estudar', 'praticar',
         'trabalhar', 'mercado', 'programador', 'futuro')

for cont in range(0, len(tupla)):
    print(f'Na palavra {tupla[cont].upper()} temos as seguintes vogais:', end='')
    for novoCont in range(0, len(tupla[cont])):
        if tupla[cont][novoCont] in 'AaEeIiOoUu':
            print(f' {tupla[cont][novoCont].upper()}', end='')
    print('.')
