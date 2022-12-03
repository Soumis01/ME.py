import pyautogui, webbrowser
from time import sleep

webbrowser.open('https://web.whatsapp.com/sed?phone=+') # Colocar numero

sleep = 20 # Espera 10 segundos para ejecutar el script

for i in range(100):
    pyautogui.typewrite('Despierta!!!')
    pyautogui.press('enter')



