jogador = dict()
elenco = []
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: ')).strip().title()
    jogador['partidas'] = int(input(f'Quantas partidas {jogador["nome"]} disputou? '))
    totalGols = 0
    gols = []
    for cont in range(0, jogador['partidas']):
        v = int(input(f'  Quantos gols fez na partida {cont+1}? '))
        gols.append(v)
        totalGols += v
    jogador['gols'] = gols
    jogador['total'] = totalGols
    if jogador['partidas'] > 0:
        jogador['media'] = jogador['total'] / jogador['partidas']
    else:
        jogador['media'] = 0
    elenco.append(jogador.copy())
    while True:
        opcao = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
        if opcao in 'SN':
            break
        print('Erro! Opção incorreta!')
    if opcao == 'N':
        break
print('-=' * 30)
print(elenco)
maiorString = 0
for k, v in enumerate(elenco):
    strTamanho = str(v["gols"])
    if len(strTamanho) > maiorString:
        maiorString = len(strTamanho)
print('-=' * 30)
print('Resumo do Elenco: ')
print(f'{"Cod":4} {"Nome":<20} {"Gols por Partida":<{maiorString}}   {"Total":>5}  {"Média":>5}')
print('-' * 100)
for k, v in enumerate(elenco):
    strTamanho = str(v["gols"])
    print(f'{k:>4} {v["nome"]:<20} {v["gols"]}{"":{maiorString - len(strTamanho)}}   {v["total"]:>5}  {v["media"]:>5.2f}')
print('-' * 100)
while True:
    busca = int(input('De qual jogador você gostaria de ver o relatório completo? '))
    if busca == 999:
        break
    elif busca >= len(elenco):
        print('Este código não existe! Digite novamente!')
    else:
        for k, v in enumerate(elenco[busca]['gols']):
            print(f'  Na {k + 1}ª partida, {elenco[busca]["nome"]} fez {v} gol(s)!')
print('<<< VOLTE SEMPRE! >>>')
