try:
    a = int(input('Numerador: '))
    b = int(input('Divisor: '))
    r = a / b
except (ValueError, TypeError):
    print(f'Infelizmente tivemos um erro :(')
    print('Você não digitou um número válido!')
except ZeroDivisionError:
    print(f'Infelizmente tivemos um erro :(')
    print('Não existe divisão por zero')
except KeyboardInterrupt:
    print(f'Infelizmente tivemos um erro :(')
    print('O usuário preferiu não informar os dados...')
except Exception as erro:
    print(f'Infelizmente tivemos um erro :(')
    print(f'O erro foi do tipo {erro.__class__}')
else:
    print(f'O resultador é {r:.1f}')
finally:
    print('Volte sempre!')
