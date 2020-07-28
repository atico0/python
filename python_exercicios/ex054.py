from datetime import date
at = date.today().year
tootma=0
tootme=0
for c in range(1,8):
    pessoas = int(input('Em que ano a {} pessoa nasceu? '.format(c)))
    idade= at - pessoas

    if idade>=21:
        tootma+=1
    else:
        tootme+=1
print("""Ao todo tivemos {} pessoas maiores de idade
e {} pessoas menores de idade""".format(tootma,tootme))

