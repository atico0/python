string = str(2**1000)
l = []
for c in string:
    l.append(int(c))
    print(c)
print(sum(l))