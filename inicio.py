from PySimpleGUI import PySimpleGUI as sg
from janelas import janela01
from janelas import jokenpo
from janelas import parouimpar
# Criar as janelas iniciais
janela01, janela02, janela03 = janela01(), None, None

# Criar loop para leitura de eventos 
while True:
    window, event, valores = sg.read_all_windows()
    if window == janela01 and event == sg.WIN_CLOSED:
        break
    if window == janela01 and event == 'JOKENPO':
        janela01.hide()
        janela02 = jokenpo()
    if window == janela02 and event == sg.WIN_CLOSED:
        janela01.un_hide()
    if window == janela01 and  event == 'PAROUIMPAR':
        janela01.hide()
        janela03 = parouimpar()
    if window == janela03 and event == sg.WIN_CLOSED:
        janela01.un_hide()
        janela01.read()
