string = ''
for k in range(30):
    for c in range(10):
        string += str(c)
print(string)


lista = [string[:10] for c in range(int(len(string)/10))]
print(lista)


string = ''
for c in range(len(lista)):
    string = string+'.'+lista[c]
string = string[1:]
print(string)
print([x + y  for x in range(10) for y in range(10,21)])