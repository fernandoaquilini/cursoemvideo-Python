tupla = ('Santos', 'Atlético-MG', 'Corinthians', 'Cuiabá', 'Internacional', 'Avaí', 'Bragantino', 'Palmeiras',
         'Flamengo', 'Coritiba', 'São Paulo', 'Botafogo', 'Fluminense', 'América-MG', 'Ceará', 'Athletico-PR',
         'Atlético-GO', 'Goiás', 'Juventude', 'Fortaleza')

print('-' * 20)
print('{:^20}'.format(' G4 '))
print('-' * 20)
for g4 in range(0, 4):
    print(f'0{g4+1} - {tupla[g4]}')
print('-' * 20)
print('\n')

print('-' * 20)
print('{:^20}'.format(' Z4 '))
print('-' * 20)
for z4 in range(len(tupla)-4, len(tupla)):
    print(f'0{z4+1} - {tupla[z4]}')
print('-' * 20)
print('\n')

print('-' * 20)
print('{:^20}'.format(' Participantes '))
print('-' * 20)
print(sorted(tupla))
print('-' * 20)

print('-' * 20)
print(f"E o maior time do mundo está na {tupla.index('São Paulo')+1}ª posição!")
print('-' * 20)

