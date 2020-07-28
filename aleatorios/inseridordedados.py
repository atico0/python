import random as rd
import pymysql.cursors

conexao = pymysql.connect(
    host='127.0.0.1',
    user = 'root',
    password='Qqqaaazzzw1Internete1',
    db='banco1',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)
cursor = conexao.cursor()

sexos = ['F','M']
prosissoes= ['prof0','prof1','prof2','prof3','prof4','prof5','prof6','prof7','prof8','prof9']
nomes = ['nome0','nome1','nome2','nome3','nome4','nome5','nome6','nome7','nome8','nome9']
sobrenomes = ['sobrenome0','sobrenome1','sobrenome2','sobrenome3','sobrenome4','sobrenome5'
    ,'sobrenome6','sobrenome7','sobrenome8','sobrenome9']


#fazedor de datas aleatorias
def a_date():
    mes = f'{rd.randint(1, 12):0>2.0f}'
    if mes !='02':
        dia= f'{rd.randint(1,30):0>2.0f}'
    else:
        dia = f'{rd.randint(1,28):0>2.0f}'
    ano = f'{rd.randint(1950,2040):}'
    data = f'{ano}-{mes}-{dia}'
    return data


#gerador de cpf
def gera_cpf():
    cpf = ""
    for c in range(11):
        cpf += f"{rd.randint(0,9)}"
    return cpf


while True:
    a = (f"insert into pessoas (cpf, nome,profi,nasc,sexo,peso,alt) values ('{gera_cpf()}',"
                 f"'{' '.join([rd.choice(nomes),rd.choice(sobrenomes)])}',"
                 f"'{rd.choice(prosissoes)}','{a_date()}','{rd.choice(sexos)}',"
                 f"{round(rd.uniform(40,140),2)},{round(rd.uniform(1.30,2.30),2)});\n")
    print(a)
    cursor.execute(a)

    conexao.commit()


cursos.close
conexao.close()
#help(pg)
