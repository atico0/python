from time import sleep
import random as rd
import pyautogui as pg

sexos = ['F','M']
prosissoes= ['prof0','prof1','prof2','prof3','prof4','prof5','prof6','prof7','prof8','prof9']
nomes = ['nome0','nome1','nome2','nome3','nome4','nome5','nome6','nome7','nome8','nome9']
sobrenomes = ['sobrenome0','sobrenome1','sobrenome2','sobrenome3','sobrenome4','sobrenome5','sobrenome6','sobrenome7','sobrenome8','sobrenome9']
#fazedor de datas aleatorias
def a_date():
    a = f'{rd.randint(1950,2090):}-{rd.randint(1,12):0>2.0f}-{rd.randint(1,31):0>2.0f}'
    return a
#gerador de cpf
def gera_cpf():
    cpf = ""
    for c in range(11):
        cpf += f"{rd.randint(0,9)}"
    return cpf

sleep(3)
while True:
    pg.typewrite(f"insert into pessoas (cpf, nome,profi,nasc,sexo,peso,alt) values ('{gera_cpf()}',"
                 f"'{' '.join([rd.choice(nomes),rd.choice(sobrenomes)])}',"
                 f"'{rd.choice(prosissoes)}','{a_date()}','{rd.choice(sexos)}',"
                 f"{round(rd.uniform(40,140),2)},{round(rd.uniform(1.30,2.30),2)});\n")
    pg.hotkey('ctrlleft','enter')
    sleep(1.5)
    cont += 1
#help(pg)







