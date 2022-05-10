def leiaDinheiro(msg):
    valid = False
    while not valid:
        s = str(input(msg)).replace(',', '.').strip()
        if s.isalpha():
            print(f'\033[0;31mA entrada \"{s}\" é um Preço INVÁLIDO\033[m')
        else:
            valid = True
            return float(s)
