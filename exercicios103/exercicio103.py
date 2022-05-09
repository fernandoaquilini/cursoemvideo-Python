# Functions
def ficha(nome='<desconhecido>', gols=0):
    return f'O jogador {nome} fez {gols} gol(s) no campeonato.'


# Main
j = str(input('Digite o nome: '))
g = str(input('Número de gols: ')).strip()
if g.isnumeric():
    g = int(g)
else:
    g = 0
if j.strip() == '':
    print(ficha(gols=g))
else:
    print(ficha(nome=j, gols=g))
