from PySimpleGUI import PySimpleGUI as sg
from jokenpo import jokenpo
from parouimpar import parouimpar
from calculadora import calculadora

# Janela inicio
def janela01():
    from PySimpleGUI import PySimpleGUI as sg
    sg.theme('Reddit')
    layout = [
        [sg.Button(f'{"JOKENPÔ":^53}', key='JOKENPO')],
        [sg.Button(f'{"PAR OU ÍMPAR":^49}', key='PAROUIMPAR')],   
        [sg.Button(f'{"CALCULADORA":^48}', key='CALCULADORA')],  
    ]
    return sg.Window('Mini Programas', layout=layout, finalize=True)

# Criar as janelas iniciais
janela01, janela02, janela03, janela04 = janela01(), None, None, None

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
    if window == janela01 and  event == 'CALCULADORA':
        janela04 = calculadora()
    if window == janela04 and event == sg.WIN_CLOSED:
        janela01.read()
        