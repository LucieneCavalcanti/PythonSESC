"""
Programa aplica na prática as funções estudadas neste material
No exemplo simulamos a navegação por uma tela, seleção e cópia
de parte do conteúdo de uma janela e posteriormente a colagem
do conteúdo em um campo de outra aplicação e o clique em um botão
para salvar as informações gravadas.
"""

import pyautogui
import pyperclip
from time import sleep
from pyperclip import paste

inicio_texto = (500, 250) #Substituir coordenadas pelo início do texto a copiar
final_texto = (480, 250) #Substituir coordenadas pelo início do texto a copiar
campo_da_app = (550, 400) #Substituir coordenadas pelo local do campo a receber a cópia
botao_salvar = (600, 63) #Substituir coordenadas do botão de confirmação/salvamento na aplicação

pyautogui.moveTo(inicio_texto, duration=0.5)
pyautogui.click()
pyautogui.dragTo(final_texto)
sleep(1)

pyautogui.hotkey('ctrl', 'c', logScreenshot=True)
sleep(1)

conteudo = paste()
#print (conteudo)

resposta = pyautogui.confirm('Deseja colocar o texto no campo XPTO', buttons=('Sim', 'Não'))
if resposta == 'Sim':
    pyautogui.click(campo_da_app)
    sleep(1)
    pyautogui.typewrite(conteudo)
    sleep(2)
    pyautogui.moveTo(botao_salvar, duration=0.5)
    pyautogui.click(logScreenshot=True)
