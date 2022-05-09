casa = float(input('Entre com o Valor da Casa (R$): '))
salario = float(input('Entre com o Valor do seu Salário atual (R$): '))
prazo = int(input('Entre com o número de anos para o pagamento: '))
parcela = (casa / (prazo * 12))
limite = salario * 0.3
if parcela <= limite:
    print('Parabéns, seu empréstimo foi aprovado!')
    print('Você pagará sua casa em {} meses, com parcelas de R$ {:.2f}.'.format(prazo * 12, parcela))
else:
    print('Infelizmente seu empréstimo não foi aprovado!')
    print('Você não terá condições de pagar sua casa em {} meses, com parcelas de R$ {:.2f}.'.format(prazo * 12, parcela))
