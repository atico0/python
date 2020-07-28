a=float(input('Primeiro segmento: '))
b=float(input('Segundo segmento: '))
c=float(input('Terceiro segmento: '))
if a<b+c and b<a+c and c<a+b:
    print('Os segmentos acima formam um triângulo do tipo:')
    if a==b==c:
        print('triângulo EQUILÁTERO')
    elif a==b or a==c or b==c or c==a:
        print('triângulo ISÓCELES')
    elif a!= b!= c!= a:
        print('triângulo ESCALENO')
else:
    print('Os segmentos acima NÃO pordem formar um triângulo')
