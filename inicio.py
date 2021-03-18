from PySimpleGUI import PySimpleGUI as sg

# Criar janelas e estilos (layout)
def janela_choice():
    sg.theme('Reddit')
    layout = [
        [sg.Button(f'{"JOKENPÔ":^53}', key='JOKENPO')],
        [sg.Button(f'{"PAR OU ÍMPAR":^49}', key='PAROUIMPAR')],     
    ]
    return sg.Window('JOGOS', layout=layout, finalize=True)
def janela_jokenpo():
    sg.theme('Reddit')
    layout = [
        [sg.Button(f'{"PEDRA":^48}', key='PEDRA')],
        [sg.Button(f'{"PAPEL":^49}', key='PAPEL')],
        [sg.Button(f'{"TESOURA":^46}', key='TESOURA')],        
        [sg.Output(size=(33, 6))]
        [sg.Button(f'{"Voltar":^49}', key='voltar')], 
    ]
    return sg.Window('JOKENPO', layout=layout, finalize=True)

# Criar as janelas iniciais
janela01, janela02 = janela_choice(), None

# Criar loop para leitura de eventos 
while True:
    window, event, values = sg.read_all_windows()
    if window == janela01 and event == sg.WIN_CLOSED:
        break
    if window == janela01 and event == 'PAROUIMPAR':
        janela02 = janela_jokenpo()
        janela01.hide()
    if window == janela02 and event == 'Voltar':
        jaela02.hide()
        janela01.un_hide()
        