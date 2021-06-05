from PySimpleGUI import PySimpleGUI as sg
from jokenpo import jokenpo

# Janela inicio
def janela01():
    WIN_W = 80
    WIN_H = 25
    filename = None

    sg.theme('DarkBlue14')
    layout = [
        [sg.Text(size=(WIN_W,1), background_color = '#272828')],
        [sg.Text('Digite aqui seu nome: ', size=(18, 1), font=("Helvetica", 20), background_color = '#272828', text_color='white')
        ,sg.Input(size=(20, 1), font=("Helvetica", 20), background_color = '#2f3030', text_color='white')],
        [sg.Text(size=(12,1), background_color = '#272828', text_color='white', key='-OUTPUT-')],   
        [sg.Text('\n Escolha seu Mini-Programa/Mini-Game \n ', size=(33, 3), font=("Helvetica", 24), relief=sg.RELIEF_RIDGE, background_color = 'black', text_color='#4F4F4F')],    
        [sg.Button(f'{"JOKENPÔ":^}', key='JOKENPO', size=(38, 1)), sg.Button(f'{"PAR OU ÍMPAR":^}', key='PAROUIMPAR', size=(38, 1))],
        [sg.Button(f'{"DADO":^}', key='DADO', size=(38, 1)), sg.Button(f'{"default":^}', key='default', size=(38, 1))],
        [sg.Text(size=(29, 1), background_color = '#272828'), sg.Cancel(size=(20,1))]  
    ]
    return sg.Window('Jogramas',
    layout=layout,
    resizable=True,
    return_keyboard_events=True,
    finalize=True,
    icon= 'image/icons/icon_main.png',
    background_color = '#272828')

# Janela do segundo jogo (par ou impar)
def parouimpar(): 
    from PySimpleGUI import PySimpleGUI as sg
    from random import randint
    import os

    # layout
    sg.theme('DarkBlue14')
    layout = [
        [sg.Text(f'{"VOCÊ ESCOLHER PAR OU ÍMPAR?":^28}', background_color = '#4F4F4F')],
        [sg.Radio(f' {"PAR":^15}', "escolha1", default=True, background_color = '#4F4F4F'),
        sg.Radio(f' {"IMPAR":^15}', "escolha1", background_color = '#4F4F4F')],
        [sg.Text('Digite seu número aqui: ', background_color = '#4F4F4F'), sg.Input(size=(9, 1))],
        [sg.Button(f'{"START":^44}')],
    ]
    # janela
    janela = sg.Window('PAR OU IMPAR',
    layout,
    background_color = '#4F4F4F',
    icon= 'image/icons/icon_parouimpar.png'
    )

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
                janela.hide()
                sg.popup(f'Voce escolheu o numero {valores[2]}\nPC escolheu o numero: {pc_number}\nA soma foi: {sum} ({result})\nSua escolha: {usu_choose}\nEscolha do PC: {pc_choose}\n{"GANHOU, JOGUE NOVAMENTE!":^20}', title = 'GANHOU', text_color = 'green', background_color = '#4F4F4F', no_titlebar=True)
                janela.UnHide()
                cont += 1
            else:
                janela.hide()
                sg.popup(f'Voce escolheu o numero {valores[2]}\nPC escolheu o numero: {pc_number}\nA soma foi: {sum} ({result})\nSua escolha: {usu_choose}\nEscolha do PC: {pc_choose}\n{"PERDEU OTARIO!":^20}\nVocẽ GANHOU {cont} vezes.', title = 'PERDEU', text_color = 'red', background_color = '#4F4F4F', no_titlebar=True)
                janela.UnHide()
                cont = 0
            break
    return(sg.Window('PAR OU ÍMPAR', finalize=True))

# Janela do Dado
def dado():
    from PySimpleGUI import PySimpleGUI as sg
    from random import randint

    # Define a animação
    def gif():
        gif = 'image/dado/dadogiratorio.gif'
        for i in range(20000):
            sg.popup_animated(gif, no_titlebar=True, time_between_frames=100, background_color = '#4F4F4F')
        sg.popup_animated(None)
        return gif

    # Define a janela principal
    def janela01():
        WIN_W = 80
        WIN_H = 25
        filename = None
        sg.theme('DarkBlue14')
        layout = [
            [sg.Image('image/dado/0.png', background_color = '#4F4F4F')],
            [sg.Button(f'{"JOGAR DADO":^38}', key='jogar')]
            ]
        window = sg.Window('Dado',
        layout=layout,
        resizable=True,
        return_keyboard_events=True,
        finalize=True,
        background_color='#4F4F4F',
        icon= 'image/dado/0.png',
        margins=(0,0))
        return window

    # Define a janela de resultado
    def janela02():
        WIN_W = 80
        WIN_H = 25
        filename = None
        resultadoDado = randint(1, 6)

        sg.theme('DarkBlue14')
        layout = [
            [sg.Button(f'{"JOGAR NOVAMENTE":^}', key='jogar', size=(29,1))],
            [sg.Image(f'image/dado/{resultadoDado}.png', background_color = '#4F4F4F')],
            [sg.Cancel(size=(29,1))],
            ]
        window = sg.Window('Dado',
        layout=layout,
        resizable=True,
        return_keyboard_events=True,
        finalize=True,
        background_color='#4F4F4F',
        margins=(0,0),
        no_titlebar=True)
        return window

    # Criar as janelas iniciais
    window = janela01()

    # Criar loop para leitura de eventos 
    while True:
        window, event, valores = sg.read_all_windows(timeout=1)
        if window == window and event in (sg.WIN_CLOSED, 'Cancel'):
            break
        if window == window and event == 'jogar':
            window.hide()
            gif()
            janela02()
    window.close()
    return window
    
# -------------------------------------------------------------------------

# Criar as janelas iniciais
janela01, janela02, janela03, janela04, janlea05 = janela01(), None, None, None, None

# Criar loop para leitura de eventos 
while True:
    window, event, valores = sg.read_all_windows(timeout=1)
    if window == janela01 and event in (sg.WIN_CLOSED, 'Cancel'):
        break
    if window == janela01 and event == 'JOKENPO':
        janela01.hide()
        janela02 = jokenpo()
        janela01.UnHide()
    if window == janela01 and  event == 'PAROUIMPAR':
        janela01.hide()
        janela03 = parouimpar()
        janela01.UnHide()
    if window == janela01 and  event == 'default':
        janela01.hide()
        janela04 = 'default'
        janela01.UnHide()
    if window == janela01 and event == 'DADO':
        janela01.hide()
        janela05 = dado()
        janela01.UnHide()
window.close()
