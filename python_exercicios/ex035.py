print('-='*20)
print('Analisador de triângulos')
print('-='*20)
a=float(input('Primeiro segmento: '))
b=float(input('Segundo segmento: '))
c=float(input('Terceiro segmento: '))
if b-c<a<b+c and a-c<b<a+b and a-b<c<a+b:
    print('Os segmentos acima PODEM formar um triângulo')
else:
    print('Os segmentos acima NÃO PODEM formar um triângulo')


