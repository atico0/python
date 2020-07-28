def cadastro ():
    arquivo = open('Lista.txt', 'a')
    nome = input('Digite seu nome: ')
    idade = input('Digite sua idade: ')
    arquivo.write(f'nome: {nome:<10}      idade: {idade:} anos\n')
    arquivo.close()
