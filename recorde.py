def recorde():
    from PySimpleGUI import PySimpleGUI as sg

    WIN_W = 80
    WIN_H = 25

    def janela_recorde():
        sg.theme('DarkBlue14')
        layout = [
                [sg.Text(size=(WIN_W,1), background_color = '#272828')],
                [sg.Text('Digite aqui seu nome: ', size=(18, 1), font=("Helvetica", 20), background_color = '#272828', text_color='white', key='nome')
                ,sg.Input(size=(20, 1), font=("Helvetica", 20), background_color = '#2f3030', text_color='white')],
                [sg.Button('Entrar', size=(80, 3), key='Enter')]
            ]

        return sg.Window('Nome',
        layout=layout,
        resizable=False,
        return_keyboard_events=True,
        finalize=True,
        icon= 'image/icons/icon_main.png',
        background_color = '#272828')

    # -------------------------------------------------------------------------
    # Criar as janelas iniciais

    janela01 = janela_recorde()

    # -------------------------------------------------------------------------
    # Criar loop para leitura de eventos 

    while True:
        window, event, valores = sg.read_all_windows(timeout=1)
        if window == janela01 and event in (sg.WIN_CLOSED, 'Cancel'):
            break
        if window == janela01 and event == 'Enter':
            janela01.hide()
            nome = str(valores[0]).capitalize()
            print(nome)
            break
    window.close()

    return sg.window('Nome', finalize=True)
    