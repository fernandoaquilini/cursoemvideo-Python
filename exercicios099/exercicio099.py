from time import sleep


def maior(* núm):
    print('-=' * 30)
    print('Analisnado os valores dos parâmetros...')
    print(f'Parâmetros: ', end='')
    numMaior = 0
    for c in range(0, len(núm)):
        print(f' {núm[c]} ', end='')
        sleep(0.3)
        if núm[c] > numMaior:
            numMaior = núm[c]
    print(f', num total de {len(núm)}.')
    print(f'O maior valor foi {numMaior}.')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()


