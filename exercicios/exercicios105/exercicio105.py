# Functions
def notas(* n, sit=False):
    """
    -> Função para analisar notas e situação de N alunos.
        :param n: (TUPLA) de 0 a N notas.
        :param sit: (OPCIONAL). Resultado da análise.
    :return: (DICIONÁRIO)
    """
    r = dict()
    if len(n) > 0:
        r['Total'] = len(n)
        r['Maior'] = max(n)
        r['Menor'] = min(n)
        r['Média'] = f'{(sum(n) / len(n)):.2f}'
        if sit:
            if 0 <= r['Média'] < 5:
                r['Situação'] = 'RUIM'
            elif 5 <= r['Média'] < 7:
                r['Situação'] = 'RAZOÁVEL'
            elif 7 <= r['Média'] < 10:
                r['Situação'] = 'BOA'
            else:
                r['Situação'] = 'EXCELENTE'
    else:
        r['ERRO'] = 'Nenhuma nota inforamda!'
    return r


resp = notas(5.6, 4, 8, 9)
print(resp)

resp = notas(5.6, 4, 8, 9, 7, 9.8, 4.2, 1, sit=True)
print(resp)

resp = notas(10, 10, 10, 10, sit=True)
print(resp)

resp = notas()
print(resp)
