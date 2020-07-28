from random import randint
l = [0,0,0,0,0,0,0,0,0,1]
cont = cont0 = cont1 = 0
while True:
    esc = randint(0,9)
    if esc != 9:
        cont0 += 1
    else:
        cont1 +=1
    cont +=1
    print(l[esc])
    print(f'cont0%={cont0/cont}, cont1%={cont1/cont} total={cont}')