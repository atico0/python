from ex115_modulo_a import cadastro
from ex115_modulo_b import  ler
while True:
    print('-'*30)
    print('MENU PRINTCIPAL'.center(30))
    print('-'*30)
    try:
        resposta = int(input('''1 - ver pessoas cadastradas
2 - Cadastrar novas pessoas
3 -  sair do sistema: '''))
    except:
        print('Erro. Digite novamente')
    else:
        if resposta == 1:
             ler()
        elif resposta == 2:
            cadastro()
        elif resposta == 3:
            break