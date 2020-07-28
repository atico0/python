import sqlite3

conexao = sqlite3.connect('basededados.db')
cursor = conexao.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS clientes ('
               'id INTEGER PRIMARY KEY AUTOINCREMENT,'
               'nome TEXT,'
               'peso REAL'
               ')'
               )
cursor.execute('INSERT INTO clientes (nome, peso) VALUES (?, ?)', ('marques da silva', 90.5))
cursor.execute('INSERT INTO clientes (nome, peso) VALUES (:nome, :peso)',
               {'nome': 'aleatorio', 'peso': 9.5})
cursor.execute(
    'INSERT INTO clientes  VALUES (:id, :nome, :peso)',
    {'id': None, "nome": 'aleatorio2', 'peso': 900.5})
conexao.commit()
#cursor.execute('DELETE FROM  clientes')
# #apaga todos os dados da tabela
conexao.commit()
cursor.execute('SELECT * FROM clientes')
print(cursor.fetchall)
for c in cursor.fetchall():
    print(c)
cursor.execute("DROP TABLE clientes")
conexao.commit()


cursor.close()
conexao.close()
