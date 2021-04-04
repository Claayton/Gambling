from time import sleep
from PySimpleGUI import PySimpleGUI as sg

gif = 'dado_giratorio.gif'

# Janela inicio
def janela01():
    WIN_W = 80
    WIN_H = 25
    filename = None

    layout = [
        [sg.Image(gif)],
        [sg.Button(f'{"Jogar o Dado":^48}', key='jogar')],
        [sg.Cancel()],
    ]
    return sg.Window('Dado',
    layout=layout,
    resizable=True,
    return_keyboard_events=True,
    finalize=True)

# Criar as janelas iniciais
janela01 = janela01()

# Criar loop para leitura de eventos 
while True:
    window, event, valores = sg.read_all_windows(timeout=1)
    if window == janela01 and event in (sg.WIN_CLOSED, 'Cancel'):
        break
    if window == janela01 and event == 'jogar':
        while True:
            [sg.popup_animated(gif,  time_between_frames=50)],
            if window == janela01 and event in (sg.WIN_CLOSED, 'Cancel'):
                break

window.close()
