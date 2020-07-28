from Contas import *
import sb


class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, valor):
        self._idade = valor

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, valor):
        self._nome = valor.title()


class Cliente(Pessoa):
    def __init__(self, nome, idade, conta):
        super().__init__(nome, idade)
        self.conta = conta

    def checa_saca(self, n):
        resposta = sb.Banco.checar(self)
        if resposta:
            self.conta.sacar(n)
        else:
            print('Dados não constam no nosso banco de dados')

    def infos(self):
        print(f'Nome: {self.nome}; Idade: {self.idade}')
        self.conta.infos()
