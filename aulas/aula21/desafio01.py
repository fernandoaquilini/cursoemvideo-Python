from datetime import date


# Functions
def voto(ano=0):
    if ano <= 0:
        return 'Ano Inválido. Digite Novamente!'
    else:
        idade = date.today().year - ano
        if 1 <= idade < 16:
            return f'Com {idade} anos: VOTO PROIBÍDO!'
        elif 16 <= idade < 18:
            return f'Com {idade} anos: VOTO OPCIONAL!'
        elif 18 <= idade < 66:
            return f'Com {idade} anos: VOTO OBRIGATÓRIO!'
        else:
            return f'Com {idade} anos: VOTO OPCIONAL!'


# Main
print('-' * 20)
ano = int(input('Em que ano você nasceu? '))
print(voto(ano))
