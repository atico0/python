from pessoas import *
class Banco:
    def __init__(self):
        pass

    agencias = []
    nomes = []
    contas = []

    @classmethod
    def adicionar_cliente(cls, clitente):
        cls.nomes.append(clitente.nome)
        cls.contas.append(clitente.conta)
        cls.agencias.append(clitente.conta.agencia)

    @classmethod
    def listar_clientes(cls):
        for c in range(len(cls.nomes)):
            print(f'Nome: {cls.nomes[c]}; Conta: {cls.contas[c]}; Agencia: {cls.agencias[c]}')

    @classmethod
    def checar(cls, pedinte):
        condicao1 = pedinte.conta.agencia in Banco.agencias
        condicao2 = pedinte.conta in Banco.contas
        condicao3 = pedinte.nome in Banco.nomes
        condicao4 = Banco.nomes.index(pedinte.nome) == Banco.contas.index(pedinte.conta) == Banco.agencias.index(
            pedinte.conta.agencia)
        if condicao4 and condicao3 and condicao2 and condicao1:
            return True
        return None
