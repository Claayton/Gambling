from PySimpleGUI import PySimpleGUI as sg
from jokenpo import jokenpo
from dado import dado
from parouimpar import parouimpar
from recorde import recorde
import buttons

# -------------------------------------------------------------------------
# Janela inicial


def janela_inicio():
    WIN_W = 80
    WIN_H = 25

    sg.theme('DarkBlue14')
    layout = [
        [sg.Canvas(background_color='black', size=(650, 10), pad=None)],
        [sg.Text(' \n           TESTE SUA SORTE\n ', size=(26, 3), font=('mood', 30), background_color = '#272828', text_color='white')],    
        [sg.Canvas(background_color='black', size=(650, 10), pad=None)],
        [sg.Canvas(background_color='#272828', size=(30, 150), pad=None),
        sg.Button('', image_data=buttons.button_jokenpo, key='JOKENPO', button_color=(sg.theme_background_color('#4f4f4f'), sg.theme_background_color('#4f4f4f')), border_width=0.5),
        sg.Canvas(background_color='#272828', size=(30, 150), pad=None), 
        sg.Button('', image_data=buttons.button_poui64, key='PAROUIMPAR', button_color=(sg.theme_background_color('#4f4f4f'), sg.theme_background_color('#4f4f4f')), border_width=0.5),
        sg.Canvas(background_color='#272828', size=(30, 150), pad=None), 
        sg.Button('', image_data=buttons.button_dado64, key='DADO', button_color=(sg.theme_background_color('#4f4f4f'), sg.theme_background_color('#4f4f4f')), border_width=0.5),
        sg.Canvas(background_color='#272828', size=(30, 150), pad=None)],
        [sg.Canvas(background_color='black', size=(650, 10), pad=None)]
    ]

    return sg.Window('Jogramas',
    layout=layout,
    resizable=True,
    return_keyboard_events=True,
    finalize=True,
    icon= 'imagens/icon_main.png',
    background_color = '#272828')


# -------------------------------------------------------------------------
# Criar as janelas iniciais

janela01, janela02, janela03, janela04, janela05 = recorde(), None, None, None, None

# -------------------------------------------------------------------------
# Criar loop para leitura de eventos 

while True:
    window, event, valores = sg.read_all_windows(timeout=1)
    if window == janela01 and event in (sg.WIN_CLOSED, 'Cancel', 'Enter'):
        janela02 = janela_inicio()
    if window == janela02 and event in (sg.WIN_CLOSED, 'Cancel'):
        break
    if window == janela02 and event == 'JOKENPO':
        janela02.hide()
        janela03 = jokenpo()
        janela02.UnHide()
    if window == janela02 and  event == 'PAROUIMPAR':
        janela02.hide()
        janela04 = parouimpar()
        janela02.UnHide()
    if window == janela02 and event == 'DADO':
        janela02.hide()
        janela05 = dado()
        janela02.UnHide()
window.close()
