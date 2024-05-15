from PySimpleGUI import *  # Importa todos os comandos da biblioteca para a GUI
import serial              # Importa a biblioteca pyserial
from time import sleep     # Importa a biblioteca para criar delays no código


while True:  # Laço para conexão com o Arduino
    try:  # Tenta se conectar ao Arduino
        arduino = serial.Serial('COM4', 9600)  # Cria um elemento conectado a porta COM4
        break

    except Exception:  # Se não for possível, imprime a mensagem e dá um delay de 1 segundo
        print('Não foi possível se conectar ao Arduino')
        sleep(1)

estado = 'Alarme desligado'

layout = [[Text(estado, justification='center', key='estado')], # Estado do alarme
          [Button('Ligar/Desligar', size=(14, 2))]]  # Botão para ligar/desligar o alarme 

janela = Window('Controlador', layout, size=(400,75), element_justification='center')  # Cria a janela

while True:  # Laço para o envio do comandos
    eventos, valores = janela.Read()  # Leitura dos valores e eventos da tela
    cmd = ''  # Comando a ser enviado

    if eventos == WINDOW_CLOSED:  # Checa se a janela é fechada
        break

    # Verifica se o botão foi pressionado
    if eventos == 'Ligar/Desligar':
        if estado == 'Alarme desligado':
            cmd = 'l'
            estado = 'Alarme ligado'
        else:
            cmd = 'd'
            estado = 'Alarme desligado'    


    # Atualiza na tela o estado do alarme
    janela.find_element('estado').Update(estado)

    arduino.write(cmd.encode())  # Envia o comando
    arduino.flush() #Limpa o serial
