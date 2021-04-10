from PySimpleGUI import PySimpleGUI as sg

# Janela inicio
def janela01():
    WIN_W = 80
    WIN_H = 25
    filename = None

    sg.theme('DarkBlue14')
    layout = [
        [sg.Text(size=(WIN_W,1), background_color = '#4F4F4F')],
        [sg.Text('Digite aqui seu nome: ', size=(18, 1), font=("Helvetica", 20), background_color = '#4F4F4F', text_color='white')
        ,sg.Input(size=(20, 1), font=("Helvetica", 20), background_color = 'white', text_color='black')],
        [sg.Text(size=(12,1), background_color = '#4F4F4F', text_color='white', key='-OUTPUT-')],   
        [sg.Text('\n Escolha seu Mini-Programa/Mini-Game \n ', size=(33, 3), font=("Helvetica", 24), relief=sg.RELIEF_RIDGE, background_color = 'black', text_color='#4F4F4F')],    
        [sg.Button(f'{"JOKENPÔ":^}', key='JOKENPO', size=(38, 1)), sg.Button(f'{"CALCULADORA":^}', key='CALCULADORA', size=(38, 1))],
        [sg.Button(f'{"PAR OU ÍMPAR":^}', key='PAROUIMPAR', size=(38, 1)), sg.Button(f'{"DADO":^}', key='dado', size=(38, 1))],
        [sg.Text(size=(29, 1), background_color = '#4F4F4F'), sg.Cancel(size=(20,1))]  
    ]
    return sg.Window('Jogramas',
    layout=layout,
    resizable=True,
    return_keyboard_events=True,
    finalize=True,
    background_color = '#4F4F4F')

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
    janela = sg.Window('JOKENPÔ', layout, background_color = '#4F4F4F')

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
                sg.popup(f'{"JO":-^40}', title = 'JO', auto_close = True, auto_close_duration = 0.5, no_titlebar=True, background_color = '#4F4F4F')
                sg.popup(f'{"KEN":-^40}', title = 'KEN', auto_close = True, auto_close_duration = 0.5, no_titlebar=True, background_color = '#4F4F4F')
                sg.popup(f'{"PÔ":-^40}', title = 'PÔ', auto_close = True, auto_close_duration = 0.5, no_titlebar=True, background_color = '#4F4F4F')
                sg.popup(f'Você escolheu: {p1escolha}\nE o computador escolheu: {pcescolha}\n{result}', title = 'RESULTADO', no_titlebar=True, background_color = '#4F4F4F')
                janela.UnHide()
            break 
    return(sg.Window('JOKENPÔ', finalize=True))

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
    janela = sg.Window('PAR OU IMPAR', layout, background_color = '#4F4F4F')

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

# Janela da calculadora
def calculadora():
    from PySimpleGUI import PySimpleGUI as sg
    # layout
    sg.theme('DarkBlue14')
    layout = [

        [sg.Input(size=(20, 2))], 
        [sg.Button(f'{"7":^3}', key='7'), sg.Button(f'{"8":^3}', key='8'), sg.Button(f'{"9":^3}', key='9'), sg.Button(f'{"/":^3}', key='/')],
        [sg.Button(f'{"6":^3}', key='6'), sg.Button(f'{"5":^3}', key='5'), sg.Button(f'{"4":^3}', key='4'), sg.Button(f'{"*":^3}', key='*')],
        [sg.Button(f'{"1":^3}', key='1'), sg.Button(f'{"2":^3}', key='2'), sg.Button(f'{"3":^3}', key='3'), sg.Button(f'{"-":^3}', key='-')],
        [sg.Button(f'{"0":^3}', key='0'), sg.Button(f'{".":^4}', key='.'), sg.Button(f'{"=":^3}', key='='), sg.Button(f'{"+":^3}', key='+')]
    ]
    # janela
    janela = sg.Window('Calculadora', layout, background_color = '#4F4F4F')

    # ler eventos 
    while True:
        eventos, valores = janela.read()
        if eventos == sg.WINDOW_CLOSED:
            break


# Criar as janelas iniciais
janela01, janela02, janela03, janela04 = janela01(), None, None, None

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
    if window == janela01 and  event == 'CALCULADORA':
        janela01.hide()
        janela04 = calculadora()
        janela01.UnHide()
    if window == janela01 and event == 'DADO':
        janela01.hide()
        janela05 = dado()
        janela01.UnHide()
window.close()
