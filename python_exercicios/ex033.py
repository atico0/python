p=int(input('Primeiro valor: '))
s=int(input('Segundo valor: '))
t=int(input('Terceiro valor'))
if p>s and p>t:
    print('O maior valor digitado foi {}'.format(p))
if s>p and s>t:
    print('O maior valor digitado foi {}'.format(s))
if t>p and t>s:
    print('O maior valor digitado foi {}'.format(t))
if p<s and p<t:
    print('O menor valor digitado foi {}'.format(p))
if s<p and s<t:
    print('O menor valor digitado foi {}'.format(s))
if t<p and t<s:
    print('O menor valor digitado foi {}'.format(t))
if p==s and p==t:
    print('Todos os valores são iguais')