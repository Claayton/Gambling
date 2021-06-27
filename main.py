from PySimpleGUI import PySimpleGUI as sg
from jokenpo import jokenpo
from dado import dado
from parouimpar import parouimpar
import buttons

# -------------------------------------------------------------------------
# Janela inicial


def janela01():
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
    icon= 'image/icons/icon_main.png',
    background_color = '#272828')


# -------------------------------------------------------------------------
# Criar as janelas iniciais

janela01, janela02, janela03, janela04, janlea05 = janela01(), None, None, None, None

# -------------------------------------------------------------------------
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
    if window == janela01 and event == 'DADO':
        janela01.hide()
        janela05 = dado()
        janela01.UnHide()    
    if window == janela01 and  event == 'default':
        janela01.hide()
        janela04 = 'default'
        janela01.UnHide()
window.close()
