from pyautogui import *
from time import sleep

url = 'https://br.investing.com/commodities/carbon-emissions-historical-data'

PAUSE = 1
press('win')
sleep(1)
write('Chrome')
sleep(1)
press('enter')
sleep(2)
write(url)
sleep(1)
press('enter')
