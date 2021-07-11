def parouimpar(): 
    from PySimpleGUI import PySimpleGUI as sg
    from random import randint

    # layout
    sg.theme('DarkBlue14')
    layout1 = [
        [sg.Text(f'{"VOCÊ ESCOLHER PAR OU ÍMPAR?":^28}', background_color = '#4F4F4F')],
        [sg.Radio(f' {"PAR":^15}', "escolha1", default=True, background_color = '#4F4F4F'),
        sg.Radio(f' {"IMPAR":^15}', "escolha1", background_color = '#4F4F4F')],
        [sg.Text('Digite seu número aqui: ', background_color = '#4F4F4F'), sg.Input(size=(9, 1))],
        [sg.Button(f'{"Enter":^44}')],
    ]

    layout = layout1
    # janela
    janela = sg.Window('PAR OU IMPAR',
    layout,
    background_color = '#4F4F4F',
    icon= 'imagens/parouimpar/icon_parouimpar.png'
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