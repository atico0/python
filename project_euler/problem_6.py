sq = qs = 0
for c in range(101):
    sq += (c**2)
    qs += c
qs = qs**2
dif = qs - sq
print(dif)