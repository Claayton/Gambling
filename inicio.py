from PySimpleGUI import PySimpleGUI as sg
from jokenpo import jokenpo
from parouimpar import parouimpar

# Criar janelas e estilos (layout)
def janela_choice():
    sg.theme('Reddift')
    layout = [
        [sg.Button(f'{"JOKENPÔ":^53}', key='JOKENPO')],
        [sg.Button(f'{"PAR OU ÍMPAR":^49}')],     
    ]
    return sg.Window('JOGOS', layout=layout, finalize=True)

# Criar as janelas iniciais
janela01, janela02, janela03 = janela_choice(), None, None

# Criar loop para leitura de eventos 
while True:
    window, event, values =   all_windows.read
    if window == janela01 and event == sg.WIN_CLOSED:
        break
    if window == janela01 and event == 'JOKENPO':
        janela01.hide()
        janlea02 = jokenpo()
    if window == janela01 and  event == 'PAR OU ÍMPAR':
        janela01.hide()
        janela03 = parouimpar()
    if window == janela02 and event == sg.WIN_CLOSED:
        janela02.hide()
        janela01.un_hide()
        