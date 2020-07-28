import playsound
from time import sleep

tempo = int(input('Quanto tempo até o alarme tocar? min: '))
sleep(tempo *60)
while True:
    playsound.playsound('Blood Water.mp3')


# alarme simples
