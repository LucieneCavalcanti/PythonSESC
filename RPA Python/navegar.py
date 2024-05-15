#Bibliotecas usadas
import pyautogui
from time import sleep
icone_navegador = (400, 746)
campo_busca = (205, 47)
resultado = (399, 292)
termoBusca = 'VideosdaLuciene YouTube'
email='luciene.etec@gmail.com'

##===============================
#RPA
##===============================
#Passo 1: Abrir navegador
pyautogui.moveTo(icone_navegador, duration=1)
pyautogui.sleep(1)
pyautogui.click()
pyautogui.sleep(2)
#Passo 2: Realizar busca
pyautogui.moveTo(campo_busca, duration=1)
sleep(0.5)
pyautogui.typewrite(termoBusca)
pyautogui.sleep(1)
pyautogui.press('enter')

# #Passo 3: Acessar resultado
pyautogui.sleep(2)
pyautogui.moveTo(resultado)
pyautogui.sleep(1)
pyautogui.click()