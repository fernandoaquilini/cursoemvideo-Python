from random import randint
from time import sleep
from operator import itemgetter
sorteio = {'Jogador 01': randint(1, 6), 'Jogador 02': randint(1, 6),
           'Jogador 03': randint(1, 6), 'Jogador 04': randint(1, 6)}
print('<<< SORTEIO >>>')
ranking = ()
for k, v in sorteio.items():
    sleep(1)
    print(f'O {k} tirou {v} no dado!')
ranking = sorted(sorteio.items(), key=itemgetter(1), reverse=True)
print('<<< RESULTADO >>>')
for k, v in enumerate(ranking):
    print(f'O {v[0]} ficou em {k + 1}º, pois tirou {v[1]} no dado!')
