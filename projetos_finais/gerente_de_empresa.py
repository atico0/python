'''
**Gerente da Empresa ** - Criar uma hierarquia de classes -
 classe abstrata Empregado e subclasses do Gerente de Trabalho,
 Gerente e Executivo da HourlyEmployee, SalariedEmployee.
O pagamento de cada um é calculado de forma diferente, pesquise um pouco sobre isso.
Depois de estabelecer uma hierarquia de funcionários, crie uma
classe da empresa que permita gerenciar os funcionários.
Você deve ser capaz de contratar, demitir e contratar funcionários.
'''
from abc import ABC, abstractclassmethod


class Empregado(ABC):
    @abstractclassmethod
    def __init__(self, nome):
        self.nome = nome

    def __(self):
        print(self.nome)


class GerenteDeTrabalho(Empregado):
    def __init__(self, nome):
        super().__init__(nome)


class Gerente(Empregado):
    def __init__(self, nome):
        super().__init__(nome, )


class Executivo(Empregado):
    def __init__(self, nome):
        super().__init__(nome)


class HourlyEmployee:
    def __init__(self, trabalhador, dinheiro):
        self.trabalhador = trabalhador
        self.dinheiro = dinheiro

    def calculo(self, horas):
        return self.dinheiro * horas


class SalariedEmployee:
    def __init__(self, trabalhador, dinheiro):
        self.trabalhador = trabalhador
        self.dinheiro = dinheiro

    def calculo(self):
        return self.dinheiro * 160


class Empresa:
    def __init__(self, nome):
        self.nome = nome
        self.funcionarios = {}

    def demitir(self, funcionario):
        print(f'{funcionario.trabalhador.nome} Demitido')
        del (self.funcionarios[funcionario])

    def contratar(self, funcionario):
        print(f'{funcionario.trabalhador.nome} contratado')
        self.funcionarios.update({funcionario: funcionario.calculo(10)})


jegue = HourlyEmployee(Gerente('luis'), 5)

emp1 = Empresa('apple')
emp1.contratar(jegue)
print(emp1.funcionarios)
emp1.demitir(jegue)
print(emp1.funcionarios)
