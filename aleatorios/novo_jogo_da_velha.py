# Variavei predefinidas
p1 = p2 = p3 = p4 = p5 = p6 = p7 = p8 = p9 = ' '  # posiçoes do tabuleiro
escolhas = [p1, p2, p3, p4, p5, p6, p7, p8, p9]  # lista com as posiçoes
vitorias1 = 0  # vitorias do jogador um
vitorias2 = 0  # """"""""""""""""" dois
empates = 0
vez = 0  # variavel usada para saber quem vai jogar
status = ''  # variavel usada para saber se houve um ganhador ou empatou
jogadas1 = []  # lista de jogadas do jogador 1
jogadas2 = []  # """""""""""""""""""""""""""" 2
cont = 0  # variavel usada para no while da rodada se o status for empate ou alguem ganhar ela recebe 1


# TABULEIRO

def tabuleiro(lista):
    print(f'''                {lista[0]} |  {lista[1]}  | {lista[2]}
             _____|_____|_____
                {lista[3]} |  {lista[4]}  | {lista[5]}
             _____|_____|_____
               {lista[6]}  |  {lista[7]}  | {lista[8]}
                  |     |''')


# def pra limpar o tabuleiro e a lista com jogadas dos players
def limpeza(lista):
    for limpador in range(len(lista)):
        lista[limpador] = ' '


# def para saber quem ganhou usando as listas com suas jogadas
def ganhador(lista):
    if 1 in lista and 2 in lista and 3 in lista:
        return 'GANHOU'
    elif 4 in lista and 5 in lista and 6 in lista:
        return 'GANHOU'
    elif 7 in lista and 8 in lista and 9 in lista:
        return 'GANHOU'
    elif 1 in lista and 4 in lista and 7 in lista:
        return 'GANHOU'
    elif 2 in lista and 5 in lista and 8 in lista:
        return 'GANHOU'
    elif 3 in lista and 6 in lista and 9 in lista:
        return 'GANHOU'
    elif 3 in lista and 5 in lista and 7 in lista:
        return 'GANHOU'
    elif 1 in lista and 5 in lista and 9 in lista:
        return 'GANHOU'


print('JOGO DA VELHA')
print('ESCOLHA ONDE VAI JOGAR PELAS POSIÇÕES NÚMERICAS DO TABUELIRO')
tabuleiro(escolhas)
# Jogadores
jog_1 = str(input('Primeiro jogador: '))
jog_2 = str(input('Segundo jogador: '))
if jog_1 == jog_2:
    while jog_2 == jog_1:
        jog_2 = input('Nome ja usado então troca saporra ai: ')

dicio = {jog_1: 'O', jog_2: 'X'}
while True:
    while cont == 0:
        if vez >= 9 and ' ' not in escolhas:
            status = 'EMPATE'
            empates += 1
            cont = 1
            if dicio[jog_1] == 'O':
                dicio = {jog_2: 'O', jog_1: 'X'}
            else:
                dicio = {jog_1: 'O', jog_2: 'X'}
        elif vez % 2 == 0:
            jogada = input(f'Escolha sua jogada {jog_1}: ')
            while not jogada.isnumeric():
                jogada = input('Jogada invalida. Jogue novamente: ')
            jogada = int(jogada)
        else:
            jogada = input(f'Escolha sua jogada {jog_2}: ')
            while not jogada.isnumeric():
                jogada = input('Jogada invalida. Jogue novamente: ')
            jogada = int(jogada)
        if jogada > 9:
            print('Jogada invalida pff jogue dnv')
            vez -= 1
        elif escolhas[jogada - 1] != ' ':
            print('Jogada invalida pff jogue dnv')
            vez -= 1
        elif vez % 2 == 0:
            escolhas[jogada - 1] = dicio[jog_1]
            jogadas1.append(jogada)
            status = f'{jog_1} {ganhador(jogadas1)}'
        else:
            escolhas[jogada - 1] = dicio[jog_2]
            jogadas2.append(jogada)
            status = f'{jog_2} {ganhador(jogadas2)}'
        tabuleiro(escolhas)
        vez += 1
        if 'GANHOU' in status or 'EMPATE' in status:
            cont = 1
        if status == f'{jog_1} GANHOU':
            vitorias1 += 1
            dicio = {jog_1: 'O', jog_2: 'X'}
        elif status == f'{jog_2} GANHOU':
            vitorias2 += 1
            dicio = {jog_2: 'O', jog_1: 'X'}

    print(status)
    continuar = str(input('Desejam continuar? [S/N]')).strip().upper()
    if continuar[0] == 'N':
        break
    elif continuar == 'S':
        print('JOGO RECOMEÇANDO')
        limpeza(jogadas1)
        limpeza(jogadas2)
        limpeza(escolhas)
        tabuleiro(escolhas)
        cont = 0
        if status == f'{jog_1} GANHOU':
            vez = 0
        elif status == f'{jog_2} GANHOU':
            vez = 1
        elif status == 'EMPATE':
            if dicio[jog_1] == 'O':
                vez = 0
            else:
                vez = 1
    else:
        while continuar != 'S' and continuar != 'N':
            continuar = str(input('Não entendi. Desejam continuar? [S/N]')).strip().upper()
print(status)
print(f'{jog_1} venceu {vitorias1} e {jog_2} venceu {vitorias2} e tiveram {empates} empates')
if vitorias1 > vitorias2:
    print(f'{jog_1} É O VENCEDOR')
elif vitorias2 > vitorias1:
    print(f'{jog_2} É O VENCEDOR')
else:
    print('EMPATOU')
