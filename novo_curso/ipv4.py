conversores = [128, 64, 32, 16, 8, 4, 2, 1]  # usados para converter numeros de binarios pra decimais

#função pra converter uma lista de strings com numeros binarios e uma lista de decimais
def dec(binarios):
    decimais = []
    masc_conver = []
    for c in binarios:
        for k in range(len(c)):
            decimais.append(int(c[k]) * conversores[k])
        masc_conver.append(str(sum(decimais)))
        decimais = []
    return masc_conver


ipv4 = input('Digite o ipv4: ')  # ip
ip = ipv4.replace('/', '.').split('.')
print(ip)

hosts = int(ip[-1])  # número de 1's que vai a mascara de sub red vai ter
hosts_r = hosts_rdr= hosts
del (ip[-1])  # ele não é usado nessa parte do calculo
print(ip)
# conversão dos números do ip pra binario
ip_bin = []
for c in range(len(ip)):
    ip_bin.append(str(bin(int(ip[c]))[2:]))  # só pega a partir do 2 pq os numeros binarios no python comçam com 0b
    # todos binarios precissam ter 8 digitos e os que não tem são preenchidos com 0's
    while len(ip_bin[c]) < 8:
        ip_bin[c] = '0' + ip_bin[c]
print(ip_bin)

#numero de hots
nh = 2 ** (32 - hosts) - 2

# calculo da mascara de sub rede
n_bits = 32
masc = []
for c in range(4):
    bit = ''
    for k in range(8):

        if hosts > 0:
            bit = bit + '1'
        else:
            bit = bit + '0'
        hosts = hosts - 1
    masc.append(bit)

# conversão da mascara que estava binarios pra decimais
masc_conver = dec(masc)
print(masc)
print(masc_conver)


# ip da rede
ip_rede = []
for c in ip_bin:
    ip_rede_elemento = ''
    for k in c:
        if hosts_r > 0:
            ip_rede_elemento = ip_rede_elemento + k
        else:
            ip_rede_elemento = ip_rede_elemento + '0'
        hosts_r = hosts_r - 1
    ip_rede.append(ip_rede_elemento)
print(ip_rede)
ip_rede_deci = dec(ip_rede)
#ip da rede brodcast
ip_bro = []
for c in ip_bin:
    ip_rede_elemento = ''
    for k in c:
        if hosts_rdr > 0:
            ip_rede_elemento = ip_rede_elemento + k
        else:
            ip_rede_elemento = ip_rede_elemento + '1'
        hosts_rdr = hosts_rdr - 1
    ip_bro.append(ip_rede_elemento)
print(ip_bro)
ip_bro_deci = dec(ip_bro)

#prints
ipf = ipredef = ip_brof = ''
for c in range(len(ip)):
    ipf += ip[c] + ' '
    ipredef += ip_rede_deci[c] + ' '
    ip_brof += ip_bro_deci[c] + ' '
print(f'ip: {ipf}')
print(f'ip da rede: {ipredef}')
print(f'ip brodcast: {ip_brof}')
print(f"Número de ip's da rede: {nh}")