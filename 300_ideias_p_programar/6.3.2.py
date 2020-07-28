carac_morse = {'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.', 'g': '--.', 'h': '....', 'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---', 'p': '.--.', 'q': '--.-', 'r': '.-.', 's': '...', 't': '-', 'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-', 'y': '-.--', 'z': '--..','0':'-----','1':'.----','2':'..---','3':'...--','4':'....-','5':'.....','6':'-....','7':'--...','8':'---..','9':'----.',' ':'/','':' ','.':'.-.-.-',',':'--..--','?':'..--..',"'":'.----.','!':'-.-.--'}
morse_carac = dict()
for k, v in carac_morse.items():
    morse_carac[v] = k
frase = input('Digite uma frase: ').lower()
escolha = input('P/ converter de caracteres para morse Digite 1; P/ converter de morse para caracere digite 2: ')
while escolha != '1' and escolha != '2':
    escolha = input('Não entendi. Digite novamente: ')
nova_frase = ''
if escolha == '1':
    for c in frase:
        if c in carac_morse:
            nova_frase = nova_frase+ carac_morse[c]+' '
elif escolha == '2':
    for c in frase.split():
        if c in morse_carac:
            nova_frase = nova_frase + morse_carac[c]+' '
print(nova_frase)
