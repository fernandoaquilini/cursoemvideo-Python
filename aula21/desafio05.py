# Functions
def notas(* n, sit=False):
    """
    -> Função para analisar notas e situação de N alunos.
        :param n: (TUPLA) de 0 a N notas.
        :param sit: (OPCIONAL). Resultado da análise.
    :return: (DICIONÁRIO)
    """
    resp = dict()
    if len(n) > 0:
        total = soma = maior = menor = 0
        for c in range(0, len(n)):
            total += 1
            soma += n[c]
            if c == 0:
                maior = menor = n[c]
            else:
                if n[c] > maior:
                    maior = n[c]
                if n[c] < menor:
                    menor = n[c]
        resp['Total'] = total
        resp['Maior'] = maior
        resp['Menor'] = menor
        media = soma / total
        resp['Média'] = f'{(soma / total):.2f}'
        if sit:
            if 0 <= media < 5:
                resp['Situação'] = 'RUIM'
            elif 5 <= media < 7:
                resp['Situação'] = 'RAZOÁVEL'
            elif 7 <= media < 10:
                resp['Situação'] = 'BOA'
            else:
                resp['Situação'] = 'EXCELENTE'
    else:
        resp['ERRO'] = 'Nenhuma nota inforamda!'
    return resp


resp = notas(5.6, 4, 8, 9)
print(resp)

resp = notas(5.6, 4, 8, 9, 7, 9.8, 4.2, 1, sit=True)
print(resp)

resp = notas(10, 10, 10, 10, sit=True)
print(resp)

resp = notas()
print(resp)
