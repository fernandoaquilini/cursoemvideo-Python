jogador = dict()
jogador['nome'] = str(input('Nome do jogador: ')).strip().title()
jogador['partidas'] = int(input(f'Quantas partidas {jogador["nome"]} disputou? '))
total = 0
gols = []
for cont in range(0, jogador['partidas']):
    v = int(input(f'Quantos gols fez na partida {cont+1}? '))
    gols.append(v)
    total += v
jogador['gols'] = gols
jogador['total'] = total
jogador['media'] = jogador['total'] / jogador['partidas']
print('-=' * 20)
print(jogador)
print('-=' * 20)
for k, v in jogador.items():
    print(f'O campo {k.capitalize()} tem o valor {v}.')
print('-=' * 20)
print(f'O jogador {jogador["nome"]} jogou {jogador["partidas"]} partidas.')
for cont in range(0, len(jogador['gols'])):
    print(f'   => Na partida {cont+1}, fez {jogador["gols"][cont]} gol(s).')
print(f'Foi um total de {jogador["total"]} gol(s) e uma média de {jogador["media"]:.2f} gols/partida.')
