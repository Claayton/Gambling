from PySimpleGUI import PySimpleGUI as sg
from random import randint

# Define a animação
def gif():
    gif = 'image/dadogiratorio.gif'
    for i in range(20000):
        sg.popup_animated(gif, no_titlebar=True, time_between_frames=100, background_color = '#4F4F4F')
    sg.popup_animated(None)
    return gif

# Define a janela principal
def janela01():
    WIN_W = 80
    WIN_H = 25
    filename = None
    sg.theme('DarkBlue14')
    layout = [
        [sg.Button(f'{"JOGAR DADO":^38}', key='jogar')],
        [sg.Image('image/0.png', background_color = '#4F4F4F')]
        ]
    window = sg.Window('Dado',
    layout=layout,
    resizable=True,
    return_keyboard_events=True,
    finalize=True,
    background_color='#4F4F4F',
    margins=(0,0), icon = 'icone')
    return window

# Define a janela de resultado
def janela02():
    WIN_W = 80
    WIN_H = 25
    filename = None
    resultadoDado = randint(1, 6)

    sg.theme('DarkBlue14')
    layout = [
        [sg.Button(f'{"JOGAR DADO":^38}', key='jogar')],
        [sg.Image(f'image/{resultadoDado}.png', background_color = '#4F4F4F')]
        ]
    window = sg.Window('Dado',
    layout=layout,
    resizable=True,
    return_keyboard_events=True,
    finalize=True,
    background_color='#4F4F4F',
    margins=(0,0), icon = 'icone')
    return window

# Criar as janelas iniciais
window = janela01()

# Criar loop para leitura de eventos 
while True:
    window, event, valores = sg.read_all_windows(timeout=1)
    if window == window and event in (sg.WIN_CLOSED, 'Cancel'):
        break
    if window == window and event == 'jogar':
        window.hide()
        gif()
        janela02()
window.close()
