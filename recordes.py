def recordes():
    import PySimpleGUI as sg
    from funçoes import consulta_dados

    def janela_recorde():
        
        win_w = 650
        win_h = 450
        bgcolor = '#4F4F4F'
        ccolor = 'black'

        sg.theme('DarkBlue14')
        layout = [
            [sg.Canvas(background_color=bgcolor, size=(650, 20))],
            [sg.Text('RECORDES', size=(70, 1), font=("Arial", 30), background_color=bgcolor, text_color='white', key='nome', justification='center')],
            [sg.Canvas(background_color='black', size=(650, 2))],
            [sg.Canvas(background_color=bgcolor, size=(650, 30))],
            [sg.Text(f'JOKENPOH               PAR OU ÍMPAR        DADO', size=(70, 1), font=("Dyuthi", 20), background_color=bgcolor, text_color='white', key='ouro')],
            [sg.Canvas(background_color='black', size=(650, 2))],
            [sg.Canvas(background_color=bgcolor, size=(650, 15))],

            [sg.Text(f'Nome: {consulta_dados(classificacao="ouro")[1]}\nMédia de vitórias: {consulta_dados(classificacao="ouro")[6]:.1f}%', size=(30, 2), font=("Arial", 10), background_color=bgcolor, text_color='#DAA520', justification='left'),
                sg.Text(f'Nome: {consulta_dados(classificacao="prata")[1]}\nMédia de vitórias: {consulta_dados(classificacao="prata")[6]:.1f}%', size=(30, 2), font=("Arial", 10), background_color=bgcolor, text_color='#DAA520', justification='left'),
                sg.Text(f'Nome: {consulta_dados(classificacao="bronze")[1]}\nMédia de vitórias: {consulta_dados(classificacao="bronze")[6]:.1f}%', size=(30, 2), font=("Arial", 10), background_color=bgcolor, text_color='#DAA520', justification='left')],
            [sg.Canvas(background_color='black', size=(650, 2))],
            [sg.Canvas(background_color=bgcolor, size=(650, 15))],

            [sg.Text(f'Nome: {"Default"}\nMédia de vitórias: {"Default"}', size=(30, 2), font=("Arial", 10), background_color=bgcolor, text_color='#A9A9A9', justification='left'),
                sg.Text(f'Nome: {"Default"}\nMédia de vitórias: {"Default"}', size=(30, 2), font=("Arial", 10), background_color=bgcolor, text_color='#A9A9A9', justification='left'),
                sg.Text(f'Nome: {"Default"}\nMédia de vitórias: {"Default"}', size=(30, 2), font=("Arial", 10), background_color=bgcolor, text_color='#A9A9A9', justification='left')],
            [sg.Canvas(background_color='black', size=(650, 2))],
            [sg.Canvas(background_color=bgcolor, size=(650, 15))],

            [sg.Text(f'Nome: {"Default"}\nMédia de vitórias: {"Default"}', size=(30, 2), font=("Arial", 10), background_color=bgcolor, text_color='#CD7F32', justification='left'),
                sg.Text(f'Nome: {"Default"}\nMédia de vitórias: {"Default"}', size=(30, 2), font=("Arial", 10), background_color=bgcolor, text_color='#CD7F32', justification='left'),
                sg.Text(f'Nome: {"Default"}\nMédia de vitórias: {"Default"}', size=(30, 2), font=("Arial", 10), background_color=bgcolor, text_color='#CD7F32', justification='left')],
            [sg.Canvas(background_color='black', size=(650, 2))],
            [sg.Canvas(background_color=bgcolor, size=(650, 10))]
            ] 

        return sg.Window('Recordes',
                         location=(350, 150),
                         size=(win_w, win_h),
                         layout=layout,
                         resizable=True,
                         return_keyboard_events=True,
                         finalize=True,
                         titlebar_icon='imagens/icon_main.png',
                         icon='imagens/icon_main.png',
                         background_color=bgcolor)

    # Criar as janelas iniciais

    janela01 = janela_recorde()

    # -------------------------------------------------------------------------

    # Criar loop para leitura de eventos 

    while True:
        window, event, valores = sg.read_all_windows(timeout=1)
        if window == janela01 and event in (sg.WIN_CLOSED, 'Cancel'):
            break
    window.close()
