lugar1 = (float(input('Digite a latitude: ')),float(input('Digite a longitude: ')))
lugar2 = (float(input('Digite a latitude: ')),float(input('Digite a longitude: ')))
distancia = ((lugar1[0]-lugar2[0])**2+(lugar1[1]-lugar2[1])**2)**0.5
print(f'A distância é {distancia}')