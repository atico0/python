from time import sleep
print('-'*30)
print('LISTAGEM DE PREÇO')
print('-'*30)
cont = 0
a = 'óculos dolce gabbana','corretinha 1','correntinha 2','BAPE','cinto OFF-WAITE'\
    ,'camisetinha preta basica','calça DISEL','turtle dove','relogio da tissot','pulseirinha'\
    ,'aneliznho',['800,00','1.500,00','4.000,000','4.000,00' ,'550,00','60,00','750,00'\
    ,'1,800,00','3.000,00','8.000,00','2.000,00',]
for c in a[0:11]:
    cont -= 1
    print(f'{c:.<30}R$ {a[11][0+cont]}')
    sleep(1.5)