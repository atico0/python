frase=str(input('Digite uma frase: ')).strip().upper()
palavras= frase.split()
junto=''.join(palavras)
inverso=''
for letra in range( len(junto)-1,-1,-1):
    inverso += junto[letra]
print('Você escreveu {}, Ao contrario fica assim: {}'.format(junto,inverso))
if inverso==junto:
        print('Temos um palíndromo!')
else:
        print('Isso NÃO é um palíndromo!')


