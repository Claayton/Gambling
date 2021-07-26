def dado():
    from PySimpleGUI import PySimpleGUI as sg
    from random import randint

    # Define a animação
    def gif():
        gif_animado = 'imagens/dado/dadogiratorio.gif'
        for i in range(20000):
            sg.popup_animated(gif_animado, no_titlebar=True, time_between_frames=100, background_color='#4F4F4F')
        return gif

    # Define a janela principal
    def janela_init():
        win_w = 80
        win_h = 25
        filename = None
        sg.theme('DarkBlue14')
        layout = [
            [sg.Image('imagens/dado/0.png', background_color='#4F4F4F')],
            [sg.Button(f'{"JOGAR DADO":^38}', key='jogar')]
            ]
        window_init = sg.Window('Dado',
                                layout=layout,
                                resizable=True,
                                return_keyboard_events=True,
                                finalize=True,
                                background_color='#4F4F4F',
                                icon='imagens/dado/0.png',
                                margins=(0, 0))
        return window_init

    # Define a janela de resultado
    def resultado():
        win_w = 80
        win_h = 25
        filename = None
        resultadodado = randint(1, 6)

        sg.theme('DarkBlue14')
        layout = [
            [sg.Button(f'{"JOGAR NOVAMENTE":^}', key='jogar', size=(29, 1))],
            [sg.Image(f'imagens/dado/{resultadodado}.png', background_color='#4F4F4F')],
            [sg.Cancel(size=(29, 1))],
            ]
        window_resultado = sg.Window('Dado',
                                     layout=layout,
                                     resizable=True,
                                     return_keyboard_events=True,
                                     finalize=True,
                                     background_color='#4F4F4F',
                                     margins=(0, 0),
                                     no_titlebar=True)
        return window_resultado

    # Criar as janelas iniciais
    janela01, janela02 = janela_init(), None

    # Criar loop para leitura de eventos 
    while True:
        window, event, values = sg.read_all_windows(timeout=1)
        if window == janela01 and event in (sg.WIN_CLOSED, 'Cancel'):
            break
        if window == janela01 and event == 'jogar':
            janela01.hide()
            janela02 = resultado()
            janela02.Hide()
            gif()
            janela02.UnHide()
        if window == janela02 and event == 'Cancel':
            break
        if window == janela02 and event == 'jogar':
            janela02.Hide()
            janela02 = resultado()
            janela02.Hide()
            gif()
            janela02.UnHide()
    window.close()
    return window
