'''
Escreva uma função chamada `choose_from_hist` que receba um histograma como definido em
“Um dicionário como uma coleção de contadores”,
na página 163, e retorne um valor aleatório do histograma,
escolhido por probabilidade em proporção à frequência. Por exemplo, para este histograma:
'''
import random


def choose_from_hist(dic):
    probs = []
    chaves = list(dic.keys())
    for c in chaves:
        for k in range(dic[c]):
            probs.append(chaves.index(c))
    escolha = random.randint(0, len(probs)-1)
    escolha = probs[escolha]
    return chaves[escolha]

e = choose_from_hist({'a':3,'b':2,'c':-1})
print(e)

