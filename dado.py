from PySimpleGUI import PySimpleGUI as sg

# Janela inicio
def janela01():
    WIN_W = 80
    WIN_H = 25
    filename = None

    layout = [
        [sg.Button(f'{"JOGAR DADO":^50}', key='jogar'), sg.Cancel()]
        ]
    return sg.Window('Dado',
    layout=layout,
    resizable=True,
    return_keyboard_events=True,
    finalize=True,
    background_color='gray',
    margins=(0,0))

# Criar as janelas iniciais
window = janela01()

# Criar loop para leitura de eventos 
while True:
    window, event = window.read()  
    if window == janela01 and event in (sg.WIN_CLOSED, 'Cancel'):
        break
    if window == janela01 and event == 'jogar':
        graph.MoveFigure(my_circle, 10, 10)
window.close()
