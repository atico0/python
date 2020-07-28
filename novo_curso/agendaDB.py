import sqlite3


class Agenda:
    def __init__(self, arquivo):
        self.conn = sqlite3.connect(f'{arquivo}.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute('CREATE TABLE IF NOT EXISTS nomes('
                            'id INTEGER PRIMARY KEY AUTOINCREMENT,'
                            'telefone INTEGER UNIQUE,'
                            'nome TEXT'
                            ')')

    def inserir(self, nome, telefone):
        self.cursor.execute(f'INSERT OR IGNORE INTO nomes (nome, telefone) VALUES (?, ?)', (f'{nome}', telefone))
        self.conn.commit()

    def editar(self, iden, nome=None, telefone=None):
        consulta = 'UPDATE OR IGNORE nomes SET nome=?, telefone=? WHERE id=?'
        self.cursor.execute(consulta, (nome, telefone, iden))

    def excluir(self, iden):
       self.cursor.execute('DELETE FROM nomes WHERE id = ? ', (iden,))

    def listar(self):
        self.cursor.execute('SELECT * FROM nomes')
        for c in self.cursor.fetchall():
            print(c)

    def limpargeral(self):
        self.cursor.execute('DELETE FROM nomes')
        self.conn.commit()

    def fechar(self):
        self.cursor.close()
        self.conn.close()


agenda = Agenda('agenda')
#agenda.limpargeral()
agenda.inserir('luis',9090)
agenda.inserir('gabriel', '9090')
agenda.listar()
agenda.editar(nome='luissss', telefone= 999, iden= 2 )
agenda.listar()
#agenda.excluir(2)
agenda.listar()
#agenda.cursor.execute('DROP TABLE nomes')
