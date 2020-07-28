s=int(input('\033[1;30;mDigite um número: '))
n=int(input('Outro número: \33[m'))
f=s+n
print('\033[4;34mA soma entre\033[;35;m {}\33[;;;m e\033[33m {}\33[m \033[4;34mvale\33[31m {}'.format(s,n,f))


   