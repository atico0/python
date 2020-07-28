#Encontre o número inteiro positivo único cujo quadrado possui o formato 1_2_3_4_5_6_7_8_9_0,
#onde cada "_" é um único dígito

#logica usada:
# eu criei 1 lista de strings que vai do 1 ao 9 e acaba com 0
# criei um contador  do número que sera submetido ao teste do seu quadrado
# um loop infinito e coloquei nele uma lista que recebe os mesmos elementos da lista do 1 ao 9

contador = 1013000110
#  (tem esse valor pq o quadrado
#  desse número é um valor proximo do menor quadrado compátivel com o quadrado pedido acima
#  "1020304050607080900")
while True:
    digitos_alteraveis = ['0']+ [str(x) for x in range(9, 0,-1)]
    impa_pa = 2
    vrf = True
    numero = str(contador**2)
    if numero[0] == '1' and numero[2] == '2' and numero[4] == '3' and numero[6] == '4' \
            and numero[8] == '5' and numero[10] == '6' and numero[12] == '7' \
            and numero[14] == '8' and numero[16] == '9' and numero[18] == '0':
            vrf = True
    else:
        vrf = False
    if vrf:

        certo = contador
        break
    elif (contador**2)>1929394959697989990:
        print('CODIGO INCORRETO')
        certo = 'ERRRRRROOOOUUUUU'
    print(contador, contador ** 2)
    contador +=1
print(f'O número é {certo} e o seu quadrado é {certo**2}')
# programa inconclusivo pq está demorando mt