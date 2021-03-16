from PySimpleGUI import PySimpleGUI as sg

# layout
sg.theme('Reddit')
layout = [
    [sg.Button(f'{"JOKENPÔ":^48}', key='JOKENPO')],
    [sg.Button(f'{"PAR OU ÍMPAR":^49}', key='PAROUIMPAR')],     
]
# janela
janela = sg.Window('JOGOS', layout)

# ler eventos 
while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'JOKENPO':
        open(jokenpo)
