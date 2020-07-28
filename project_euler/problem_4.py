pali = 0
for c in range(999,100,-1):
    for k in range(999,100,-1):
        print((c,k,k*c))
        if str(c*k) == str(c*k)[::-1]:
            pali = c*k
            break
print()
print(pali)