from PySimpleGUI import PySimpleGUI as sg
from jokenpo import jokenpo
from dado import dado
from parouimpar import parouimpar

# -------------------------------------------------------------------------
# Janela inicial


def janela01():
    WIN_W = 80
    WIN_H = 25
    filename = None


    sg.theme('DarkBlue14')
    layout = [
        [sg.Text(size=(WIN_W,1), background_color = '#272828')],
        [sg.Text('Digite aqui seu nome: ', size=(18, 1), font=("Helvetica", 20), background_color = '#272828', text_color='white')
        ,sg.Input(size=(20, 1), font=("Helvetica", 20), background_color = '#2f3030', text_color='white')],
        [sg.Text(size=(12,1), background_color = '#272828', text_color='white', key='-OUTPUT-')],   
        [sg.Text('\n Escolha seu Mini-Programa/Mini-Game \n ', size=(33, 3), font=("Helvetica", 24), relief=sg.RELIEF_RIDGE, background_color = 'black', text_color='#4F4F4F')],    
        [sg.Button(f'{"JOKENPÔ":^}', key='JOKENPO', size=(38, 1)), sg.Button(f'{"PAR OU ÍMPAR":^}', key='PAROUIMPAR', size=(38, 1))],
        [sg.Button(f'{"DADO":^}', key='DADO', size=(38, 1)), sg.Button(f'{"default":^}', key='default', size=(38, 1))],
        [sg.Text(size=(29, 1), background_color = '#272828'), sg.Cancel(size=(20,1))]  
    ]
    return sg.Window('Jogramas',
    layout=layout,
    resizable=True,
    return_keyboard_events=True,
    finalize=True,
    icon= 'image/icons/icon_main.png',
    background_color = '#272828')

# -------------------------------------------------------------------------

# Criar as janelas iniciais
janela01, janela02, janela03, janela04, janlea05 = janela01(), None, None, None, None

# Criar loop para leitura de eventos 
while True:
    window, event, valores = sg.read_all_windows(timeout=1)
    if window == janela01 and event in (sg.WIN_CLOSED, 'Cancel'):
        break
    if window == janela01 and event == 'JOKENPO':
        janela01.hide()
        janela02 = jokenpo()
        janela01.UnHide()
    if window == janela01 and  event == 'PAROUIMPAR':
        janela01.hide()
        janela03 = parouimpar()
        janela01.UnHide()
    if window == janela01 and  event == 'default':
        janela01.hide()
        janela04 = 'default'
        janela01.UnHide()
    if window == janela01 and event == 'DADO':
        janela01.hide()
        janela05 = dado()
        janela01.UnHide()
window.close()
