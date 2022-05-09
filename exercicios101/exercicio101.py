# Functions
def voto(y=0):
    from datetime import date
    if y <= 0:
        return 'Ano Inválido. Digite Novamente!'
    else:
        idade = date.today().year - y
        if 1 <= idade < 16:
            return f'Com {idade} anos: VOTO PROIBÍDO!'
        elif 16 <= idade < 18 or idade > 65:
            return f'Com {idade} anos: VOTO OPCIONAL!'
        else:
            return f'Com {idade} anos: VOTO OBRIGATÓRIO!'


# Main
print('-' * 20)
ano = int(input('Em que ano você nasceu? '))
print(voto(ano))
