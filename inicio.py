from PySimpleGUI import PySimpleGUI as sg

# Criar janelas e estilos (layout)
def janela_choice():
    sg.theme('Reddit')
    layout = [
        [sg.Button(f'{"JOKENPÔ":^53}')],
        [sg.Button(f'{"PAR OU ÍMPAR":^49}')],     
    ]
    return sg.Window('JOGOS', layout=layout, finalize=True)
def janela_jokenpo():
    sg.theme('Reddit')
    layout = [
        [sg.Button(f'{"PEDRA":^48}')],
        [sg.Button(f'{"PAPEL":^49}')],
        [sg.Button(f'{"TESOURA":^46}')],        
        [sg.Output(size=(33, 6))]
        [sg.Button(f'{"Voltar":^49}',)], 
    ]
    return sg.Window('JOKENPO', layout=layout, finalize=True)
def janela_parouimpar():
    sg.theme('Reddit')
    layout = [
        [sg.Checkbox('PAR', key='par'), sg.Checkbox('Impar', key='impar')],
        [sg]
        [sg.Button(f'{"JOKENPÔ":^53}')],
        [sg.Button(f'{"PAR OU ÍMPAR":^49}')],     
    ]
    return sg.Window('JOGOS', layout=layout, finalize=True)

# Criar as janelas iniciais
janela01, janela02 = janela_choice(), None

# Criar loop para leitura de eventos 
while True:
    window, event, values = sg.read_all_windows()
    if window == janela01 and event == sg.WIN_CLOSED:
        break
    if window == janela01 and event == 'JOKENPÔ':
        janela02 = janela_jokenpo()
        janela01.hide()
    if window == janela02 and event == 'Voltar':
        jaela02.hide()
        janela01.un_hide()
        