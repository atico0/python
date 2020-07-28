import math
num=float(input('Digite um ângulo: '))
sen= math.sin(math.radians(num))
cossen= math.cos(math.radians(num))
tangent= math.tan(math.radians(num))
print('O seno de {} é:{:.2f} \no cosseno é:{:.2f} \ne a tangete é:{:.2f}'.format(num, sen, cossen, tangent))
