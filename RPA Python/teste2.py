"""
Programa aplica na prática diversos tipos de caixa de interação
com o usuário, que poderiam ser usadas dentro de um RPA como forma
de confirmar etapas, pedir dados complementares ou alertar sobre situações
com necessidade de atenação especial.
"""

import pyautogui

k = 0
while True:
    #Senha original digitada no código apenas como exemplo.
    #Isto não é uma boa prática.
    senha = 'Janio'
    digitado = pyautogui.password(text='Digite sua senha:', title='Testa senha: Senha')

    #Lógica simples para confirmar se a senha digitada é correta
    if senha == digitado:
        pyautogui.alert(text='Senha correta', title='Testa senha: Acesso concedido')
        mensagem = pyautogui.prompt(text='Digite uma mensagem para o robô',
        title='Testa senha: Mensagem')
        confirma = pyautogui.confirm(text=f'Confirma a mensagem digitada?\n{mensagem}',
        buttons=('Sim', 'Não'), title='Testa senha: Confirmação')

        if confirma == 'Sim':
            print(f'A mensagem digitada foi: "{mensagem}".')
            break
    else:
        pyautogui.alert(text='Senha incorreta.\nTente novamente', title='Testa senha: Acesso negado')
        k += 1

    if k >= 3:
        pyautogui.alert(text='ATENÇÃO: Acesso negado.\nNúmero de tentativas excedido!',
        title='Testa senha: Acesso negado')
        print('Não houve mensagem digitada')
        break

    if k >= 1:
        print(f'Ocorreram {k} tentativas erradas de digitação da senha')
