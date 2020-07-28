tarefas = []
desfeitos = []
while True:
    esc = input('Escolha: \n[1] ADICIONAR TAREFAS\n[2]LISTAR TAREFAS\n[3]DESFAZER\n[4]REFAZER: ')

    while not esc.isnumeric():
        print('VALOR INVALIDO. DIGITE NOVAMENTE')
        esc = input('Escolha: \n[1] ADICIONAR TAREFAS\n[2]LISTAR TAREFAS\n[3]DESFAZER\n[4]REFAZER: ')
    esc = int(esc)
    if esc == 1:
        tarefas.append(input('ADICIONE SUA TAREFA:') )
    elif esc == 2:
        print('TAREFAS:')
        for c in tarefas:
            print(c)
    elif esc == 3:
        if len(tarefas) == 0:
            print('NADA A DESFAZER')
        else:
            print(f'DESFAZENDO TAREFA: {tarefas[-1]}')
            desfeitos.append(tarefas.pop())
    elif esc == 4:
        if len(desfeitos) == 0:
            print('NADA A REFAZER')
        else:
            print(f'REFAZENDO: {desfeitos[-1]}')
            tarefas.append(desfeitos.pop())