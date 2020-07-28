from time import sleep
import pyautogui as pg
hab = [(719,696),(757,697),(799,696),(839,697)]
sleep(3)
pg.click(538,737)
while True:
    pg.hotkey('Tab')
    sleep(4)
    for c in hab:
        pg.click(c)
        sleep(1)