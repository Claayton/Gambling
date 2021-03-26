# Janela do primeiro jogo (jokenpo)
def jokenpo():
    from PySimpleGUI import PySimpleGUI as sg
    from random import choice
    from time import sleep

    p1escolha = ''
    pcescolha = ''
    result = ''
    possibilidades = ['PEDRA', 'PAPEL', 'TESOURA']

    # layout
    sg.theme('Reddit')
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

# Janela do segundo jogo (par ou impar)
def parouimpar(): 
    from PySimpleGUI import PySimpleGUI as sg
    from random import randint
    import os

    # layout
    sg.theme('Reddit')
    layout = [
        [sg.Text(f'{"VOCÊ ESCOLHER PAR OU ÍMPAR?":^28}')],
        [sg.Radio(f' {"PAR":^15}', "escolha1", default=True),
        sg.Radio(f' {"IMPAR":^15}', "escolha1")],
        [sg.Text('Digite seu número aqui: '), sg.Input(size=(9, 1))],
        [sg.Button(f'{"START":^44}')],
    ]
    # janela
    janela = sg.Window('PAR OU IMPAR', layout)

    # ler eventos 
    cont = 0
    while True:
        eventos, valores = janela.read()
        if eventos == sg.WINDOW_CLOSED:
            break
        while True:
            pc_number = randint(0, 10)        
            if valores[0] == True:
                usu_choose = 'PAR'
                pc_choose = 'IMPAR'
            else:
                usu_choose = 'IMPAR'
                pc_choose = 'PAR'
            sum = int(valores[2]) + pc_number
            if sum % 2 == 0:
                result = 'PAR'
            else:
                result = 'IMPAR'  
            if usu_choose == result:
                sg.popup(f'Voce escolheu o numero {valores[2]}\nPC escolheu o numero: {pc_number}\nA soma foi: {sum} ({result})\nSua escolha: {usu_choose}\nEscolha do PC: {pc_choose}\n{"GANHOU, JOGUE NOVAMENTE!":^20}', title = 'GANHOU', text_color = 'green')
                cont += 1
            else:
                sg.popup(f'Voce escolheu o numero {valores[2]}\nPC escolheu o numero: {pc_number}\nA soma foi: {sum} ({result})\nSua escolha: {usu_choose}\nEscolha do PC: {pc_choose}\n{"PERDEU OTARIO!":^20}\nVocẽ GANHOU {cont} vezes.', title = 'PERDEU', text_color = 'red')
                cont = 0
            break
    return(sg.Window('PAR OU ÍMPAR', finalize=True))
