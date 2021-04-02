from PySimpleGUI import PySimpleGUI as sg
from jokenpo import jokenpo
from parouimpar import parouimpar
from calculadora import calculadora

# Janela inicio
def janela01():
    WIN_W = 80
    WIN_H = 25
    filename = None

    sg.theme('Reddit')
    layout = [
        [sg.Text(size=(WIN_W,1),)],
        [sg.Text('Digite aqui seu nome: ', size=(18, 1), font=("Helvetica", 20)),sg.Input(size=(19, 1), font=("Helvetica", 20))],
        [sg.Text(size=(12,1), key='-OUTPUT-')],   
        [sg.Text('Escolha seu Mini-Programa/Mini-Game', font=("Helvetica", 24), relief=sg.RELIEF_RIDGE)],    
        [sg.Button(f'{"JOKENPÔ":^53}', key='JOKENPO'), sg.Button(f'{"CALCULADORA":^48}', key='CALCULADORA')],
        [sg.Button(f'{"PAR OU ÍMPAR":^49}', key='PAROUIMPAR'), sg.Button(f'{"-INDEFINED-":^53}', key='-INDEFINED-')],
        [sg.Cancel()]  
    ]
    return sg.Window('Jogramas',
    layout=layout,
    resizable=True,
    return_keyboard_events=True,
    finalize=True)

# Criar as janelas iniciais
janela01, janela02, janela03, janela04 = janela01(), None, None, None

# Criar loop para leitura de eventos 
while True:
    window, event, valores = sg.read_all_windows(timeout=1)
    if window == janela01 and event in (sg.WIN_CLOSED, 'Cancel'):
        break
    if window == janela01 and event == 'JOKENPO':
        janela02 = jokenpo()
    if window == janela02 and event == sg.WIN_CLOSED:
        janela01 = sg.janela01()
    if window == janela01 and  event == 'PAROUIMPAR':
        janela03 = parouimpar()
    if window == janela03 and event == sg.WIN_CLOSED:
        janela01.read()
    if window == janela01 and  event == 'CALCULADORA':
        janela04 = calculadora()
    if window == janela04 and event == sg.WIN_CLOSED:
        janela01.read()
window.close()
