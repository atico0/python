def maior(* num):
    maior = num[0]
    print(num)
    for c in num:
        if maior < c:
            maior = c
    print('Foram informados {b} valores e maior valor é {a}'.format(b = len(num),a=maior))

lista = (1,2,3,4)
maior(lista )

