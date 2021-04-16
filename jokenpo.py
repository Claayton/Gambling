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
        gif = 'image/jokenpo2.gif'
        for i in range(40000):
            sg.popup_animated(gif, no_titlebar=True, time_between_frames=100, background_color = '#4F4F4F')
        sg.popup_animated(None)
        return gif

    # ler eventos 
    while True:
        eventos, valores = janela.read()
        pcescolha = choice(possibilidades)
        if eventos == sg.WINDOW_CLOSED:
            break
        while True:
            if eventos == 'PEDRA':
                p1escolha = 'PEDRA'
            elif eventos == 'PAPEL':
                p1escolha = 'PAPEL'
            elif eventos == 'TESOURA':
                p1escolha = 'TESOURA' 
            if pcescolha == p1escolha:
                result = 'EMPATE, TENTE NOVEMENTE!'
            elif pcescolha == 'PEDRA' and p1escolha == 'PAPEL' or pcescolha == 'PAPEL' and p1escolha == 'TESOURA' or pcescolha == 'TESOURA' and p1escolha == 'PEDRA':
                result = 'PARABÉNS, VOCÊ VENCEU!'
            else:
                result = 'PERDEU, TENTE NOVAMENTE!'
            if eventos == 'PEDRA' or eventos == 'PAPEL' or eventos == 'TESOURA':
                janela.hide()
                gif()
                sg.popup(f'Você escolheu: {p1escolha}\nE o computador escolheu: {pcescolha}\n{result}', title = 'RESULTADO', no_titlebar=True, background_color = '#4F4F4F')
                janela.UnHide()
            break 
    return(sg.Window('JOKENPÔ', finalize=True))