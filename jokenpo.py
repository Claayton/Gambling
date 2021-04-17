# Janela Jokenpo
def jokenpo():
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
        [sg.Button(f'{"PEDRA":^}', key='PEDRA', size=(38, 3))],
        [sg.Button(f'{"PAPEL":^}', key='PAPEL', size=(38, 3))],
        [sg.Button(f'{"TESOURA":^}', key='TESOURA', size=(38, 3))],
        [sg.Image('image/pedra.png', background_color = '#4F4F4F'),
        sg.Image('image/papel.png', background_color = '#4F4F4F'),
        sg.Image('image/tesoura.png', background_color = '#4F4F4F')],       
    ]
    # janela
    window = sg.Window('JOKENPÔ',
    layout,
    background_color = '#4F4F4F',
    icon= 'image/icons/icon_jokenpo.png')

    def jogar():
        for i in range(20000):
            sg.popup_animated(
                gif,
                no_titlebar=True,
                time_between_frames=100,
                background_color = '#4F4F4F')
        sg.popup_animated(None)
        return gif

    def resultado():
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
        eventos, values = window.read()
        pcescolha = choice(possibilidades)
        if eventos in (sg.WINDOW_CLOSED, 'Cancel'):
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
                png = 'image/jokenpo_png/pedra_pedra_result.png'
                result = 'Empate'
            elif pcescolha == 'PAPEL' and p1escolha == 'PAPEL':
                gif = 'image/jokenpo_gif/papel_papel.gif'
                png = 'image/jokenpo_png/papel_papel_result.png'
                result = 'Empate'
            elif pcescolha == 'TESOURA' and p1escolha == 'TESOURA':
                gif = 'image/jokenpo_gif/tesoura_tesoura.gif'
                png = 'image/jokenpo_png/tesoura_tesoura_result.png'
                result = 'Empate'
            
            elif pcescolha == 'PEDRA' and p1escolha == 'TESOURA':
                gif = 'image/jokenpo_gif/pedra_tesoura.gif'
                png = 'image/jokenpo_png/pedra_tesoura_result.png'
                result = 'Venceu'
            elif pcescolha == 'PAPEL' and p1escolha == 'PEDRA':
                gif = 'image/jokenpo_gif/papel_pedra.gif'
                png = 'image/jokenpo_png/papel_pedra_result.png'
                result = 'Venceu'
            elif pcescolha == 'TESOURA' and p1escolha == 'PAPEL':
                gif = 'image/jokenpo_gif/tesoura_papel.gif'
                png = 'image/jokenpo_png/tesoura_papel_result.png'
                result = 'Venceu'

            elif pcescolha == 'PEDRA' and p1escolha == 'PAPEL':
                gif = 'image/jokenpo_gif/pedra_papel.gif'
                png = 'image/jokenpo_png/pedra_papel_result.png'
                result = 'Perdeu'
            elif pcescolha == 'PAPEL' and p1escolha == 'TESOURA':
                gif = 'image/jokenpo_gif/papel_tesoura.gif'
                png = 'image/jokenpo_png/papel_tesoura_result.png'
                result = 'Perdeu'
            elif pcescolha == 'TESOURA' and p1escolha == 'PEDRA':
                gif = 'image/jokenpo_gif/tesoura_pedra.gif'
                png = 'image/jokenpo_png/tesoura_pedra_result.png'
                result = 'Perdeu'

            if eventos == 'PEDRA' or eventos == 'PAPEL' or eventos == 'TESOURA':
                window.hide()
                jogar()
                resultado()
                if eventos == 'jogar':
                    window.UnHide()
            break
    return(sg.Window('JOKENPÔ', finalize=True))
