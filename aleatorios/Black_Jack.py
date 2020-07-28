from blackjack_utilidades import *

resp = ''
mao_jog = mao()
dealer = mao()
jogador = input('Digite seu nick: ')
grana = 5000
while True:
    if grana == 0 or resp == 'N':
        break
    a = baralho('Paus', 'Copas', 'Espadas', 'Valetes')
    b = a.cartas
    cont = cont2 = apostado = apostado2 = cont_dealer = 0
    mao_jog.choice = []
    dealer.choice_dealer = []
    print('Bem vindo ao black jack')
    sleep(0.7)
    print('-=' * 30)
    print(f'Você tem {grana}R$ para apostar')
    sleep(0.7)
    print('-=' * 30)
    aposta = int(input('''Escolha sua jogada: 
    [3] Apostar
    [4] Apostar tudo: '''))
    sleep(0.7)
    print('-=' * 30)
    while aposta != 3 and aposta != 4:
        aposta = int(input('Não entendi. Digite de novo: '))
    if aposta == 3:
        quant = int(input('Quanto você quer apostar? R$'))
        sleep(1)
        print('-=' * 30)
        grana -= quant
        apostado += quant
    elif aposta == 4:
        apostado = grana
        grana = 0
    mao_jog.pegar(b, mao_jog.choice)
    mao_jog.pegar(b, mao_jog.choice)
    dealer.pegar(b, dealer.choice_dealer)
    print(f'O dealer possui a carta: {dealer.choice_dealer[0][0]} de {dealer.choice_dealer[0][1]}')
    print('-=' * 30)
    cont = contador(mao_jog.choice)
    if cont == 21:
        print('Sua mão é:')
        mostrar(mao_jog.choice)
        print('-=' * 30)
        print('VOCÊ FEZ UM BLACK JACK')
        sleep(1)
        print('-=' * 30)
        aposta = 1
    while aposta != 1 and cont < 21 and aposta != 2:
        print(f'Sua primeira  mão é:')
        sleep(0.5)
        print('-=' * 30)
        mostrar(mao_jog.choice)
        cont = contador(mao_jog.choice)
        mostra_pontos(cont)
        print('-=' * 30)
        if mao_jog.choice[0][0] == mao_jog.choice[1][0] and mao_jog.choice2 == []:
            aposta = int(input('''1 MÃO Escolha:
                                [1] Recusar
                                [2] Dobrar
                                [3] Carta
                                [4] Dividir: '''))
            sleep(1)
            print('-=' * 30)
        elif mao_jog.choice[0][0] == 10 and (
                mao_jog.choice[1][0] == 'J' or mao_jog.choice[1][0] == 'Q' or mao_jog.choice[1][0] == 'K'):
            aposta = int(input('''1 MÃO Escolha:
            [1] Recusar
            [2] Dobrar
            [3] Carta
            [4] Dividir: '''))
            sleep(1)
            print('-=' * 30)
        elif mao_jog.choice[0][0] == 'J' and (
                mao_jog.choice[1][0] == 10 or mao_jog.choice[1][0] == 'Q' or mao_jog.choice[1][0] == 'K'):
            aposta = int(input('''1 MÃO Escolha:
            [1] Recusar
            [2] Dobrar
            [3] Carta
            [4] Dividir: '''))
            sleep(1)
            print('-=' * 30)
        elif mao_jog.choice[0][0] == 'Q' and (
                mao_jog.choice[1][0] == 10 or mao_jog.choice[1][0] == 'J' or mao_jog.choice[1][0] == 'K'):
            aposta = int(input('''1 MÃO Escolha:
            [1] Recusar
            [2] Dobrar
            [3] Carta
            [4] Dividir: '''))
            sleep(1)
            print('-=' * 30)
        elif mao_jog.choice[0][0] == 'K' and (
                mao_jog.choice[1][0] == 10 or mao_jog.choice[1][0] == 'J' or mao_jog.choice[1][0] == 'Q'):
            aposta = int(input('''1 MÃO Escolha:
            [1] Recusar
            [2] Dobrar
            [3] Carta
            [4] Dividir: '''))
            sleep(1)
            print('-=' * 30)
        else:
            aposta = int(input('''1 MÃO Escolha:
                                [1] Recusar
                                [2] Dobrar
                                [3] Carta: '''))
            sleep(1)
            print('-=' * 30)
        while aposta > 4 or aposta < 1:
            aposta = int(input('Não entendi. Digite novamente: '))
            sleep(0.5)
        while aposta == 2 and grana == 0:
            aposta = input('Você não tem mais dinheiro, escolha de novo:')
        if aposta == 3:
            mao_jog.pegar(b, mao_jog.choice)
            cont = contador(mao_jog.choice)
            while aposta != 1 and cont < 21:
                print(f'Foi adicionada a carta {mao_jog.choice[-1][0]} de {mao_jog.choice[-1][1]}')
                sleep(0.5)
                print('-=' * 30)
                print('Sua mão é:')
                sleep(0.5)
                print('-=' * 30)
                mostrar(mao_jog.choice)
                print('-=' * 30)
                cont = contador(mao_jog.choice)
                mostra_pontos(cont)
                print('-=' * 30)
                aposta = int(input('Escolha: \n[1]Recusar \n[2] Carta: '))
                print('-=' * 30)
                while aposta != 1 and aposta != 2:
                    aposta = int(input('Não entendi. Digite dnv: '))
                if aposta == 2:
                    mao_jog.pegar(b, mao_jog.choice)
                    print('-=' * 30)
                    print(f'Foi adicionada a carta {mao_jog.choice[-1][0]} de {mao_jog.choice[-1][1]}')
                    print('-=' * 30)
                    print('Sua mão é:')
                    print('-=' * 30)
                    mostrar(mao_jog.choice)
                    print('-=' * 30)
                    cont = contador(mao_jog.choice)
                    mostra_pontos(cont)
                    print('-=' * 30)
        if aposta == 2 and grana > 0:
            if cont < 21:
                print('Valor apostado dobrado')
                sleep(1)
                print('-=' * 30)
                mao_jog.pegar(b, mao_jog.choice)
                print('Sua mão é')
                print('-=' * 30)
                mostrar(mao_jog.choice)
                print('-=' * 30)
                cont = contador(mao_jog.choice)
                mostra_pontos(cont)
                print('-=' * 30)
                grana -= quant
                apostado += quant
                print('-=' * 30)
                print(f'Foi adicionada a carta {mao_jog.choice[-1][0]} de {mao_jog.choice[-1][1]}')
                sleep(1)
                print('-=' * 30)
                print('Sua mão é:')
                print('-=' * 30)
                sleep(1)
                mostrar(mao_jog.choice)
                print('-=' * 30)
                cont = contador(mao_jog.choice)
                mostra_pontos(cont)
                print('-=' * 30)
        while aposta == 4 and grana == 0:
            print('Você não tem mais dinheiro para apostar, escolha de novo')
            sleep(1)
            aposta = input()
        if aposta == 4 and grana != 0:
            apostado2 += quant
            grana -= quant
            mao_jog.dividir(mao_jog.choice)
            mao_jog.pegar(b, mao_jog.choice)
            mao_jog.pegar(b, mao_jog.choice2)
            print('-=' * 30)
            print('MÃO DIVIDIDA! As suas mãos são:')
            sleep(0.5)
            print('-=' * 30)
            print('1 MÃO')
            sleep(0.5)
            mostrar(mao_jog.choice)
            print('-=' * 30)
            cont = contador(mao_jog.choice)
            mostra_pontos(cont)
            print('-=' * 30)
            print('2 MÃO')
            mostrar(mao_jog.choice2)
            cont2 = contador(mao_jog.choice2)
            mostra_pontos(cont2)
            print('-=' * 30)
            # Parte da 1 mão
            aposta = int(input('1 Mão. Escolha: \n[1]Recusar \n[2] Dobrar \n[3] Carta'))
            sleep(1)
            print('-=' * 30)
            if aposta == 3:
                while aposta != 1 and cont < 21:
                    mao_jog.pegar(b, mao_jog.choice)
                    cont = contador(mao_jog.choice)
                    print(f'Foi adicionada a carta {mao_jog.choice[-1][0]} de {mao_jog.choice[-1][1]}')
                    sleep(0.5)
                    print('-=' * 30)
                    print('Sua mão é:')
                    mostrar(mao_jog.choice)
                    print('-=' * 30)
                    mostra_pontos(cont)
                    print('-=' * 30)
                    aposta = int(input('Escolha: \n[1]Recusar \n[2] Carta'))
                    sleep(1)
                    print('-=' * 30)
                    while aposta != 1 and aposta != 2:
                        aposta = int(input('Não entendi. Digite dnv: '))
            if aposta == 2:
                mao_jog.pegar(b, mao_jog.choice)
                cont = contador(mao_jog.choice)
                print(f'Foi adicionada a carta {mao_jog.choice[-1][0]} de {mao_jog.choice[-1][1]}')
                sleep(1)
                print('-=' * 30)
                print('Sua mão é:')
                mostrar(mao_jog.choice)
                print('-=' * 30)
                mostra_pontos(cont)
                print('-=' * 30)
            # Parte da mão  2 mas vai ser só outro ctrl c ctrl v
            aposta = int(input('2 Mão. Escolha: \n[1]Recusar \n[2] Dobrar \n[3] Carta'))
            sleep(1)
            print('-=' * 30)
            if aposta == 3:
                while aposta != 1 and cont < 21:
                    mao_jog.pegar(b, mao_jog.choice2)
                    cont2 = contador(mao_jog.choice2)
                    print(f'Foi adicionada a carta {mao_jog.choice2[-1][0]} de {mao_jog.choice2[-1][1]}')
                    sleep(1)
                    print('-=' * 30)
                    print('Sua mão é:')
                    mostrar(mao_jog.choice2)
                    print('-=' * 30)
                    aposta = int(input('Escolha: \n[1]Recusar \n[2] Carta'))
                    sleep(1)
                    print('-=' * 30)
                    while aposta != 1 and aposta != 2:
                        aposta = int(input('Não entendi. Digite dnv: '))
                    cont2 = contador(mao_jog.choice2)
                    mostra_pontos(cont2)
                    print('-=' * 30)
            if aposta == 2:
                mao_jog.pegar(b, mao_jog.choice2)
                print('-=' * 30)
                print(f'Foi adicionada a carta {mao_jog.choice2[-1][0]} de {mao_jog.choice2[-1][1]}')
                print('Sua mão é:')
                mostrar(mao_jog.choice2)
                print('-=' * 30)
                cont2 = contador(mao_jog.choice2)
                mostra_pontos(cont2)
                print('-=' * 30)
    print('Sua mão 1 foi: ')
    mostrar(mao_jog.choice)
    print(f'Sua pontuação final na1 mão foi:{cont}')
    sleep(1)
    print('-=' * 30)
    if cont2 != 0:
        print('Sua mão 2 foi: ')
        mostrar(mao_jog.choice2)
        print(f'Sua pontuação final na 2 mão foi: {cont2}')
    sleep(1)
    print('-=' * 30)
    # Parte do dealer
    print('Vez do dealer')
    sleep(1)
    while cont_dealer < 17 and len(dealer.choice_dealer) <= 5 and cont_dealer <= cont:
        dealer.pegar(b, dealer.choice_dealer)
        cont_dealer = contador(dealer.choice_dealer)
        print('A mão do dealer é:')
        sleep(0.5)
        mostrar(dealer.choice_dealer)
        print('-=' * 30)
        print(f'O dealer possui {cont_dealer} pontos')
        sleep(1)
        print('-=' * 30)
    # Resultados
    x = comparar(a=cont, b=cont_dealer)
    print(f'A 1 mão {x}')
    if cont2 != 0:
        z = comparar(a=cont2, b=cont_dealer)
        print(f'A 2 mão {z}')
    else:
        z = ''
    if x == 'GANHOU':
        if len(mao_jog.choice) == 2:
            grana += (apostado * 2.5)
        else:
            grana += (apostado * 2)
    elif x == 'EMPATOU':
        grana += apostado
    elif x == 'PERDEU':
        pass
    if z == 'GANHOU':
        if len(mao_jog.choice2) == 2:
            grana += apostado2 * 2.5
        else:
            grana += apostado2 * 2
    elif z == 'EMPATOU':
        grana += apostado2
    elif z == 'PERDEU':
        pass
    apostado = apostado2 = 0
    resp = input('Quer jogar de novo? [S/N]').strip().upper()
    while not resp in 'SN':
        resp = input('Resposta invalida. Quer jogar de novo? [S/N]').strip().upper()
print('VOLTE SEMPRE')
