from PySimpleGUI import PySimpleGUI as sg
from random import randint

# Janela inicio

def jogarDado():
    resultadoDado = randint(1, 6)
    return resultadoDado

def janela01():
    WIN_W = 80
    WIN_H = 25
    filename = None

    layout = [
        [sg.Button(f'{"JOGAR DADO":^56}', key='jogar')],
        [sg.Graph(canvas_size=(300, 300), graph_bottom_left=(0, 0), graph_top_right=(400, 400), background_color='gray', enable_events=True, key='graph')],
        ]
    window = sg.Window('Dado',
    layout=layout,
    resizable=True,
    return_keyboard_events=True,
    finalize=True,
    background_color='#4F4F4F',
    margins=(0,0))

    if jogarDado == 6:
        dados = window['graph']
        dado = [
            [dados.draw_circle((80, 80), 30, fill_color='black', line_color='white')],
            [dados.draw_circle((80, 320), 30, fill_color='black', line_color='white')],
            [dados.draw_circle((320, 80), 30, fill_color='black', line_color='white')],
            [dados.draw_circle((320, 320), 30, fill_color='black', line_color='white')],
            [dados.draw_circle((320, 200), 30, fill_color='black', line_color='white')],
            [dados.draw_circle((80, 200), 30, fill_color='black', line_color='white')],
        ]

    return window

# Criar as janelas iniciais
window = janela01()

# Criar loop para leitura de eventos 
while True:
    window, event, valores = sg.read_all_windows(timeout=1)
    if window == window and event in (sg.WIN_CLOSED, 'Cancel'):
        break
    if window == window and event == 'jogar':
        jogarDado = jogarDado()
        print(jogarDado)
window.close()
