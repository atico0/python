from typing import Dict, Any, Union


def notas(*num,sit = False):
    """
    -> pega notas de alunos e retorna um dicionario
    :param num:  notas
    :param sit: (opicional) diz se a situação da turma está boa razoavel ou ruim
    :return: retorna um dicionarico contendo: A quantidade de notas; A maior nota; A menor nota e média de notas
   """
    d = dict()
    d ['Quant'] =  len(num)
    d['média'] = sum(num)/len(num)
    d['maior'] = num[0]
    d['menor'] = num[0]
    for c in num:
        if c>= d['maior']:
            d['maior'] = c
        if c<d['menor']:
            d['menor'] = c
    if sit:
        if d['média']>= 7 :
            d['situação'] = 'BOA'
        elif  7>d['média']>5:
            d['situação'] = 'RAZOAVEL'
        else:
            d['situação'] = 'RUIM'
    return d


print(notas(1,20,sit= True))

help(notas)