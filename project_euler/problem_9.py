ctop = ctad = hp = 0
com = 1
for b in range(com, 2001):
    for a in range(com + 1, 2002):
        hp = (b ** 2) + (a ** 2)
        ctad = 2 * b * a
        ctop = (a ** 2) - (b ** 2)
        print([b, a], [hp, ctop, ctad])
        if hp + ctop + ctad == 1000 :
            break
    if a != 2001:
        break
print(f'{hp} {ctad} {ctop}')
