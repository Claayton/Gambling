def recordes():
    import PySimpleGUI as sg
    from funçoes import consulta_dados


    def janela_recorde():
        
        WIN_W = 650
        WIN_H = 450
        bgcolor = '#4F4F4F'
        ccolor = 'black'
        vitórias = consulta_dados()[2]
        empates = consulta_dados()[3]
        derrotas = consulta_dados()[4]
        total = consulta_dados()[5]
        media = consulta_dados()[6]


        sg.theme('DarkBlue14')
        layout = [
            [sg.Canvas(background_color=bgcolor, size=(650, 20), pad=None)],
            [sg.Text('RECORDES', size=(70, 1), font=("Arial", 30), background_color = bgcolor, text_color='white', key='nome', justification='center')],
            [sg.Canvas(background_color='black', size=(650, 2), pad=None)],
            [sg.Canvas(background_color=bgcolor, size=(650, 30), pad=None)],
            [sg.Text(f'JOKENPOH               PAR OU ÍMPAR        DADO', size=(70, 1), font=("Dyuthi", 20), background_color = bgcolor, text_color='white', key='ouro')],
            [sg.Canvas(background_color='black', size=(650, 2), pad=None)],
            [sg.Canvas(background_color=bgcolor, size=(650, 15), pad=None)],

            [sg.Text(f'Nome: {consulta_dados(classificação="ouro")[1]}\nMédia de vitórias: {consulta_dados(classificação="ouro")[6]:.1f}%', size=(30, 2), font=("Arial", 10), background_color = bgcolor, text_color='#DAA520', justification='left'),
            sg.Text(f'Nome: {consulta_dados(classificação="prata")[1]}\nMédia de vitórias: {consulta_dados(classificação="prata")[6]:.1f}%', size=(30, 2), font=("Arial", 10), background_color = bgcolor, text_color='#DAA520', justification='left'),
            sg.Text(f'Nome: {consulta_dados(classificação="bronze")[1]}\nMédia de vitórias: {consulta_dados(classificação="bronze")[6]:.1f}%', size=(30, 2), font=("Arial", 10), background_color = bgcolor, text_color='#DAA520', justification='left')],
            [sg.Canvas(background_color='black', size=(650, 2), pad=None)],
            [sg.Canvas(background_color=bgcolor, size=(650, 15), pad=None)],

            [sg.Text(f'Nome: {"Default"}\nMédia de vitórias: {"Default"}', size=(30, 2), font=("Arial", 10), background_color = bgcolor, text_color='#A9A9A9', justification='left'),
            sg.Text(f'Nome: {"Default"}\nMédia de vitórias: {"Default"}', size=(30, 2), font=("Arial", 10), background_color = bgcolor, text_color='#A9A9A9', justification='left'),
            sg.Text(f'Nome: {"Default"}\nMédia de vitórias: {"Default"}', size=(30, 2), font=("Arial", 10), background_color = bgcolor, text_color='#A9A9A9', justification='left')],
            [sg.Canvas(background_color='black', size=(650, 2), pad=None)],
            [sg.Canvas(background_color=bgcolor, size=(650, 15), pad=None)],

            [sg.Text(f'Nome: {"Default"}\nMédia de vitórias: {"Default"}', size=(30, 2), font=("Arial", 10), background_color = bgcolor, text_color='#CD7F32', justification='left'),
            sg.Text(f'Nome: {"Default"}\nMédia de vitórias: {"Default"}', size=(30, 2), font=("Arial", 10), background_color = bgcolor, text_color='#CD7F32', justification='left'),
            sg.Text(f'Nome: {"Default"}\nMédia de vitórias: {"Default"}', size=(30, 2), font=("Arial", 10), background_color = bgcolor, text_color='#CD7F32', justification='left')],
            [sg.Canvas(background_color='black', size=(650, 2), pad=None)],
            [sg.Canvas(background_color=bgcolor, size=(650, 10), pad=None)]
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
