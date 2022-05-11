import urllib.error
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print(f'Deu erro!.')
except Exception as erro:
    print(f'Deu erro!. {erro.__class__}')
else:
    print('Ok!')
    print(site.read())
