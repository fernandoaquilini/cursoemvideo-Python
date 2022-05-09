def titulo(msg):
    print('~' * (len(msg)+4))
    print(f'{msg:^{len(msg)+4}}')
    print('~' * (len(msg)+4))


msg = str(input('Digite a sua frase: ')).strip()
titulo(msg)
