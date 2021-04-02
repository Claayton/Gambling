def jokenpo():
    from PySimpleGUI import PySimpleGUI as sg
    from random import choice
    from time import sleep

    p1escolha = ''
    pcescolha = ''
    result = ''
    possibilidades = ['PEDRA', 'PAPEL', 'TESOURA']

    # layout
    sg.theme('DarkPurple2')
    layout = [
        [sg.Button(f'{"PEDRA":^48}', key='PEDRA')],
        [sg.Button(f'{"PAPEL":^49}', key='PAPEL')],
        [sg.Button(f'{"TESOURA":^46}', key='TESOURA')],        
    ]
    # janela
    janela = sg.Window('JOKENPÔ', layout)

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
                sg.popup(f'{"JO":-^40}', title = 'JO', auto_close = True, auto_close_duration = 0.5, text_color = 'red')
                sg.popup(f'{"KEN":-^40}', title = 'KEN', auto_close = True, auto_close_duration = 0.5, text_color = 'red')
                sg.popup(f'{"PÔ":-^40}', title = 'PÔ', auto_close = True, auto_close_duration = 0.5, text_color = 'red')
                sg.popup(f'Você escolheu: {p1escolha}\nE o computador escolheu: {pcescolha}\n{result}', title = 'RESULTADO')
            break 
    return(sg.Window('JOKENPÔ', finalize=True))
