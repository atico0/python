n1=int(input('\033[7;;mDigite um valor:\033[m '))
n2=int(input('\033[7mOutro valor:\33[m '))
so=n1+n2
su=n1-n2
d=n1/n2
m=n1*n2
di=n1//n2
r=n1%n2
p=n1**n2
print('\033[31mA soma é {}, \n \033[32ma mutiplicação é {}, \n \033[33ma subtração é {}'.format(so,m,su))
print('\033[34ma divisão inteira é {}, \n \033[35ma divisão é {:.1f}, \n \033[36a potencia é {}, \n \33[37me o resto da divisão é {}'.format(di,d,p,r))
