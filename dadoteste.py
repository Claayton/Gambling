import pygame, random
from PySimpleGUI import PySimpleGUI as sg
from time import sleep

# Janela inicio
def janela01():
    WIN_W = 80
    WIN_H = 25
    filename = None

    sg.theme('Reddit')
    cont = 0
    while True:
        cont += 1
        if cont == 16:
            break
        layout = [
         [sg.Image(f'dadoframe{cont}.png')],
         [sg.Cancel()],
     ]
        sleep(0.2)
  
    return sg.Window('Dado',
    layout=layout,
    resizable=True,
    return_keyboard_events=True,
    finalize=True)

# Criar as janelas iniciais
janela01 = janela01()

# Criar loop para leitura de eventos 
while True:
    window, event, valores = sg.read_all_windows(timeout=1)
    if window == janela01 and event in (sg.WIN_CLOSED, 'Cancel'):
        break
window.close()
