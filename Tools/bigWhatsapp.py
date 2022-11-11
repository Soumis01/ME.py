import pyautogui, webbrowser
from time import sleep

webbrowser.open('https://web.whatsapp.com/sed?phone=+18293206225') # link de la pagina

sleep = 10 # Espera 10 segundos para ejecutar el script

for i in range(200):
    pyautogui.typewrite('Hola, esto es un script hecho en python jeje')
    pyautogui.press('enter')

