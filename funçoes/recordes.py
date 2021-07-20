def recordes():
    import PySimpleGUI as sg


    def janela_recorde():
        from funçoes import dados_do_jogador
        
        WIN_W = 650
        WIN_H = 450
        bgcolor = '#4F4F4F'
        ccolor = 'black'

        sg.theme('DarkBlue14')
        layout = [
            [sg.Text('RECORDES:', size=(18, 1), font=("Arial", 30), background_color = bgcolor, text_color='white', key='nome')],
            [sg.Canvas(background_color=bgcolor, size=(650, 30), pad=None)],
            [sg.Text('Medalha da Ouro:', size=(18, 1), font=("Arial", 15), background_color = bgcolor, text_color='#DAA520', key='ouro')],
            [sg.Text(f'{dados_do_jogador()}', size=(100, 1), font=("Arial", 10), background_color = bgcolor, text_color='#DAA520')],
            [sg.Canvas(background_color='black', size=(650, 2), pad=None)],
            [sg.Canvas(background_color=bgcolor, size=(650, 30), pad=None)],
            [sg.Text('Medalha de Prata:', size=(100, 1), font=("Arial", 15), background_color = bgcolor, text_color='#A9A9A9', key='prata')],
            [sg.Text(f'{dados_do_jogador()}', size=(100, 1), font=("Arial", 10), background_color = bgcolor, text_color='#A9A9A9')],
            [sg.Canvas(background_color='black', size=(650, 2), pad=None)],
            [sg.Canvas(background_color=bgcolor, size=(650, 30), pad=None)],
            [sg.Text('Medalha de bronze:', size=(100, 1), font=("Arial", 15), background_color = bgcolor, text_color='#CD7F32', key='bronze')],
            [sg.Text(f'{dados_do_jogador()}', size=(100, 1), font=("Arial", 10), background_color = bgcolor, text_color='#CD7F32')],
            [sg.Canvas(background_color='black', size=(650, 2), pad=None)],
            ] 

        return sg.Window('Recordes',
        location=(350, 150),
        size=(WIN_W, WIN_H),
        layout=layout,
        resizable=True,
        return_keyboard_events=True,
        finalize=True,
        titlebar_icon= 'imagens/icon_main.png',
        icon= 'imagens/icon_main.png',
        background_color = bgcolor)


    # Criar as janelas iniciais

    janela01 = janela_recorde()

    # -------------------------------------------------------------------------

    # Criar loop para leitura de eventos 

    while True:
        window, event, valores = sg.read_all_windows(timeout=1)
        if window == janela01 and event in (sg.WIN_CLOSED, 'Cancel'):
            break
    window.close()
