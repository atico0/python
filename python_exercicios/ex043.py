peso=float(input('Digite seu peso em Kg: '))
altura=float(input('Digite sua altura em metros: '))
imc=peso/(altura**2)
print('O IMC dessa pessoa é de {:.1f}'.format(imc))
if imc<18.5:
    print("Você está ABAIXO DO PESO!!")
elif 25>imc>=18.5:
    print('Parabéns você está no peso ideal!!')
elif 30>imc>=25:
    print('Você está com SOBREPESO')
elif 40>=imc>=30:
    print('Você está com OBESIDADE!!')
else:
    print('Você está com OBESIDADE MÓRBIDA')

