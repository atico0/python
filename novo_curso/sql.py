import pymysql.cursors

conexao = pymysql.connect(
    host='127.0.0.1',
    user = 'root',
    password='Qqqaaazzzw1Internete1',
    db='clientes',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)
cursor = conexao.cursor()
cursor.execute('USE clientes')
cursor.execute('INSERT INTO clientes (id, nome) VALUE '\
               '(NULL,NULL), (NULL, "EU")')
conexao.commit()

cursor.execute("SELECT * from clientes ORDER BY id DESC")
for c in cursor.fetchall():
    print(c)




cursor.close()
conexao.close()