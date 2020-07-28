import urllib
import urllib.request
try:
    a = urllib.request.urlopen('http://pudim.com.br/')
except:
    print('O site não está acessivel')
else:
    print('Site acessado com sucesso')