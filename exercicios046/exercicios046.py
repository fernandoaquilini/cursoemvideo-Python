from time import sleep
from datetime import date
ano = date.today().year
for cont in range(10, 0, -1):
    print('{}!!'.format(cont))
    sleep(1)
print('Feliz {}!!'.format(ano + 1))
