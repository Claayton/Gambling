# Janela Jokenpo

from PySimpleGUI import PySimpleGUI as sg
from random import choice
from time import sleep

p1escolha = ''
pcescolha = ''
result = ''
possibilidades = ['PEDRA', 'PAPEL', 'TESOURA']

# layout
sg.theme('DarkBlue14')
layout = [
    [sg.Button(f'{"PEDRA":^48}', key='PEDRA')],
    [sg.Button(f'{"PAPEL":^49}', key='PAPEL')],
    [sg.Button(f'{"TESOURA":^46}', key='TESOURA')],        
]
# janela
janela = sg.Window('JOKENPÔ',
layout,
background_color = '#4F4F4F',
icon= 'image/icon_jokenpo.png')

def gif():
    for i in range(25000):
        sg.popup_animated(gif, no_titlebar=True, time_between_frames=100, background_color = '#4F4F4F')
    sg.popup_animated(None)
    return gif

def png():
    WIN_W = 80
    WIN_H = 25
    filename = None

    sg.theme('DarkBlue14')
    layout = [
        [sg.Button(f'{"JOGAR NOVAMENTE":^}', key='jogar', size=(29,1))],
        [sg.Image(png, background_color = '#4F4F4F')],
        [sg.Cancel(size=(29,1))],
        ]
    window = sg.Window('Jokenpo',
    layout=layout,
    resizable=True,
    return_keyboard_events=True,
    finalize=True,
    background_color='#4F4F4F',
    margins=(0,0),
    no_titlebar=True)
    return window


# ler eventos 
while True:
    eventos, valores = janela.read()
    pcescolha = choice(possibilidades)
    if eventos == sg.WINDOW_CLOSED:
        break
    while True:
        if eventos == 'PEDRA' :
            p1escolha = 'PEDRA'
        elif eventos == 'PAPEL':
            p1escolha = 'PAPEL'
        elif eventos == 'TESOURA':
            p1escolha = 'TESOURA' 

        if pcescolha == 'PEDRA' and p1escolha == 'PEDRA':
            gif = 'image/jokenpo_gif/pedra_pedra.gif'
            png = 'image/jokenpo)png/pedra_pedra.png'
            result = 'Empate'
        elif pcescolha == 'PAPEL' and p1escolha == 'PAPEL':
            gif = 'image/jokenpo_gif/papel_papel.gif'
            png = 'image/jokenpo)png/papel_papel.png'
            result = 'Empate'
        elif pcescolha == 'TESOURA' and p1escolha == 'TESOURA':
            gif = 'image/jokenpo_gif/tesoura_tesoura.gif'
            png = 'image/jokenpo)png/tesoura_tesoura.png'
            result = 'Empate'
        
        elif pcescolha == 'PEDRA' and p1escolha == 'TESOURA':
            gif = 'image/jokenpo_gif/pedra_tesoura.gif'
            png = 'image/jokenpo)png/pedra_tesoura.png'
            result = 'Venceu'
        elif pcescolha == 'PAPEL' and p1escolha == 'PEDRA':
            gif = 'image/jokenpo_gif/papel_pedra.gif'
            png = 'image/jokenpo)png/papel_pedra.png'
            result = 'Venceu'
        elif pcescolha == 'TESOURA' and p1escolha == 'PAPEL':
            gif = 'image/jokenpo_gif/tesoura_papel.gif'
            png = 'image/jokenpo)png/tesoura_papel.png'
            result = 'Venceu'

        elif pcescolha == 'PEDRA' and p1escolha == 'PAPEL':
            gif = 'image/jokenpo_gif/pedra_papel.gif'
            png = 'image/jokenpo)png/pedra_papel.png'
            result = 'Perdeu'
        elif pcescolha == 'PAPEL' and p1escolha == 'TESOURA':
            gif = 'image/jokenpo_gif/papel_tesoura.gif'
            png = 'image/jokenpo)png/papel_tesoura.png'
            result = 'Perdeu'
        elif pcescolha == 'TESOURA' and p1escolha == 'PEDRA':
            gif = 'image/jokenpo_gif/tesoura_pedra.gif'
            png = 'image/jokenpo)png/tesoura_pedra.png'
            result = 'Perdeu'

        if eventos == 'PEDRA' or eventos == 'PAPEL' or eventos == 'TESOURA':
            janela.hide()
            gif()
            png()
            janela.UnHide()
        break 
#return(sg.Window('JOKENPÔ', finalize=True))
