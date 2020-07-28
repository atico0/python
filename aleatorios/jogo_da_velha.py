rodadas = 0
contemp = cont1 = cont2 = 0
cont = 1
vez2 = 0
vez1 = 0
rodada = ''
vencedor = 1
c = 2
p1 = ' '
#p2 = ['2 =','']
p2 = ' '
p3 = ' '
p4 = ' '
p5 = ' '
p6 = ' '
p7 = ' '
p8 = ' '
p9 = ' '
tabuleiro =[p1, p2, p3, p4, p5, p6, p7, p8, p9,'|','-']
jogador_1 = input('Jogador 1 insira seu nome: ')
jogador_2 = input('Jogador 2 insira seu nome: ')
escolha_1= []
escolha_2 =[]
def limpeza():
    p1 = ' '
    p2 = ' '
    p3 = ' '
    p4 = ' '
    p5 = ' '
    p6 = ' '
    p7 = ' '
    p8 = ' '
    p9 = ' '
    return tabuleiro
print(f'Os jogadores registrados foram {jogador_1} = O e {jogador_2} = X')
print('''Neste jogo da velha vocês terão de escrever o
número correspondente ao lugar onde querem marcar o X ou O de acordo com o tabuleiro''')
def impressao():
   return print(f'''{tabuleiro[0]} |   {tabuleiro[1]}  | {tabuleiro[2]}
  |      |
 -----------
{tabuleiro[3]} |   {tabuleiro[4]}  | {tabuleiro[5]}
  |      |
 -----------
{tabuleiro[6]} |  {tabuleiro[7]}   |{tabuleiro[8]}
  |      |      |               ''')
impressao()

while True:
    if c == (11*cont)-(cont-1):
        cont +=1
        contemp +=1
        rodadas+=1
        print(' EMPATE!!!')
        rodada = input('Desejam jogar novamente? [S/N]').upper().strip()[0]
        while rodada not in 'SN':
            rodada = input('Não entendi. Deseja jogar novamente? [S/N]').upper().strip()[0]
        if rodada[0] == 'N':
            break
        else:
            limpeza()
            impressao()
            c+=1
    elif c%2 == 0:
        print(f'{jogador_1}(O) é a sua vez escolha onde deseja jogar: ')
        vez1 =int(input(''))
        if tabuleiro[vez1-1] == ' ':
            tabuleiro[vez1-1] = 'O'
            escolha_1.append(vez1)
            print(f'{jogador_1} jogou no {vez1}')
            impressao()
        else:
            while True:
                vez1= int(input('Jogada invalida. Este lugar ja foi escolhido. Tente novamente: '))
                if tabuleiro[vez1-1]== ' ':
                    tabuleiro[vez1-1]='O'
                    escolha_1.append(vez1)
                    print(f'{jogador_1} jogou np {vez1}')
                    impressao()
                    break

    elif c%2>0:
        print(f'{jogador_2}(X) é a sua vez. Escolha onde deseja jogar')
        vez2 = int(input(''))
        if tabuleiro[vez2-1] == ' ':
            tabuleiro[vez2-1] = 'X'
            escolha_2.append(vez2)
            print(f'{jogador_2} jogou no {vez2}')
            impressao()
        else:
            while True:
                vez2 = int(input('Jogada invalida. Este lugar ja foi escolhido. Tente novamente:  '))
                if tabuleiro[vez2-1] == ' ':
                    tabuleiro[vez2-1] = 'X'
                    escolha_2.append(vez2)
                    print(f'{jogador_2} jogou no {vez2}')
                    impressao()
                    break
    if escolha_1.count(1)==escolha_1.count(2)==escolha_1.count(3)==1 or escolha_1.count(1)== escolha_1.count(4)==escolha_1.count(7)==1 or escolha_1.count(1)==escolha_1.count(5)==escolha_1.count(9)==1 or escolha_1.count(2)==escolha_1.count(5)==escolha_1.count(8)==1 or escolha_1.count(3)==escolha_1.count(6)==escolha_1.count(9)==1 or escolha_1.count(4)== escolha_1.count(5)==escolha_1.count(6)==1 or escolha_1.count(7)==escolha_1.count(8)==escolha_1.count(9)==1 or escolha_1.count(7)==escolha_1.count(5)==escolha_1.count(3)==1:
        c = 1
        cont1+=1
        rodadas += 1
        print(f'{jogador_1} VENCEU!!!')
        impressao()
        rodada =input('Desejam jogar novamente? [N/S]').upper().strip()[0]
        while not rodada in 'SN':
            rodada = input('Não entendi. Desejam jogar novamente? [N/S]').strip().upper()[0]
        if rodada == 'N':
            break
        elif rodada =='S':
             escolha_1 =[]
             limpeza()
             impressao()
    elif escolha_2.count(1)==escolha_2.count(2)==escolha_2.count(3)==1 or escolha_2.count(1)==escolha_2.count(4)==escolha_2.count(7)==1 or escolha_2.count(1)==escolha_2.count(5)==escolha_2.count(9)==1 or escolha_2.count(2)==escolha_2.count(5)==escolha_2.count(8)==1 or escolha_2.count(3)==escolha_2.count(6)==escolha_2.count(9)==1 or escolha_2.count(4)==escolha_2.count(5)==escolha_2.count(6)==1 or escolha_2.count(7)==escolha_2.count(8)==escolha_2.count(9)==1 or escolha_2.count(7)==escolha_2.count(5)==escolha_2.count(3)==1:
        rodadas +=1
        cont2+=1
        c= 2
        print(f'{jogador_2} VENCEU!!!')
        impressao()
        rodada = input('Desejam jogar novamente? [N/S]').strip().upper()[0]
        while not rodada in 'SN':
            rodada = input('Não entendi. Desejam jogar novamente?').strip.upper()[0]
            if rodada == 'N':
                break
            elif rodada =='S':
                escolha_2 = []
                limpeza()
                print('Jogo RECOMEÇANDO')
                impressao()
    c +=1
print(f'Foram jogadas {rodadas} rodadas  sendo {contemp} delas empates, {cont1} vitorias do jogador 1 ({jogador_1})  e {cont2} do jogador_2 ({jogador_2}) ')