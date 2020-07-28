class Educado:
    var_d_class = 'varivavel da classe'  # Essa varivavel existe para tds as varivaveis dessa class

    def __init__(self, comprimentador, comprimentado):
        self.comprimentador = comprimentador  # O comprimentador do lado esquerdo da igualdade é um atributo já o da direita é o paramêtro da função init e mesmo tendo os msms nomes não são iguais
        variavel = 'dasdasdasd'  # ao definir um atributo (uma var dentro de uma class) dentro de um metodo(uma func dentro de uma class)  sem o self. antes faz com que o atributo só esteja disponivel dentro do metodo
        print(variavel)

    def falador(self):
        print('ola')

    def mostra_var(self):
        print(self.var_d_class)


a = Educado('eu', 'demais')
b = Educado(1, 2)
a.comprimentado = 'demais'  # essa é outra forma de definir atributos mas dessa forma só a variavel a obtem esse atributo
print(a.comprimentador)
print(a.comprimentado)
# Os 3 exs abaixo fazem a msm coisa mas geralmente só se usa a 1
a.falador()
Educado.falador(a)
# a.falador(a)
# O  3 só funciona se definirmos a func(falador) como uma função sem limite de args
# print(Educado.variavel) não funciona
print()
print(a.var_d_class)
print(b.var_d_class)
print(Educado.var_d_class)  # Igual as linhas acima
print()
a.var_d_class = 'vai mudar'
print(a.var_d_class)
print(b.var_d_class)
print(Educado.var_d_class)
print()  # mudar o atribt a.var_da_class só altera a
Educado.var_d_class = 'agr vai mudar?'
print(a.var_d_class)
print(b.var_d_class)
print(Educado.var_d_class)
print()  # já ao mudar o atributo diretamente da class todas as variaveis dessa classe mudam mas curiosamente o a não mudou (eu suponho que seja pq ele já foi alterado antes e não é mais igual)
print(b)
a.algoai = 'algo ai'
print(a.__dict__)
print(Educado.__dict__)
print(b.__dict__)