from PySimpleGUI import PySimpleGUI as sg
from janelas import jokenpo
from janelas import parouimpar

# Janela inicio
def janela01():
    from PySimpleGUI import PySimpleGUI as sg
    sg.theme('Reddit')
    layout = [
        [sg.Button(f'{"JOKENPÔ":^53}', key='JOKENPO')],
        [sg.Button(f'{"PAR OU ÍMPAR":^49}', key='PAROUIMPAR')],     
    ]
    return sg.Window('JOGOS', layout=layout, finalize=True)

# Criar as janelas iniciais
janela01, janela02, janela03 = janela01(), None, None

# Criar loop para leitura de eventos 
while True:
    window, event, valores = sg.read_all_windows()
    if window == janela01 and event == sg.WIN_CLOSED:
        break
    if window == janela01 and event == 'JOKENPO':
        janela02 = jokenpo()
    if window == janela02 and event == sg.WIN_CLOSED:
        janela01 = sg.janela01()
    if window == janela01 and  event == 'PAROUIMPAR':
        janela03 = parouimpar()
    if window == janela03 and event == sg.WIN_CLOSED:
        janela01.read()
