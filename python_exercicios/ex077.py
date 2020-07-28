palavras = 'um','dois','zebra','hexa','brasil','revanche','milf','aprendizagem'
for c in palavras:
    print(f'\nNa palavra {c} temos ',end='')
    for letra in c:
        if letra in 'aeiou':
            print(letra,end='')

