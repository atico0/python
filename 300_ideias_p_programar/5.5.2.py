def semana(n):
    f = '-feira'
    semanas = ['Domingo', 'segunda' + f, 'Terça' + f, 'Quarta' + f, 'Quinta' + f, 'Sexta' + f, 'Sábado']
    return semanas[n - 1]


print(f'Você digitou o mês : {semana()}')
