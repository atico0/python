l1 = []
l2 = []
ls = []
for c in range(10):
    if c <= 5:
        l1.append(c)
    l2.append(c)

#SOLUÇÃO 1


soma = 0

for k,v in list(zip(l1,l2)):
    ls.append(k + v)
print(l1,l2,ls)
ls = []


#SOLUÇÃO 2


for c in range(len(l1)):
    ls.append(l1[c]+l2[c])
print(l1,l2,ls)


#SOLUÇÃO 3


ls = list(zip(l1,l2))
for c in range(len(ls)):
    ls[c] = sum(ls[c])
print(l1,l2,ls)